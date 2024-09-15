from flask import Flask, render_template, redirect, url_for, request, flash, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from main import perform_scan
from reports.generate_report import generate_report
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from datetime import datetime

app = Flask(__name__)

# app config and database
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Innit db
db = SQLAlchemy(app)

# configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    vulnerabilities = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('reports', lazy=True))

class Vulnerability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    status = db.Column(db.String(50), nullable=False, default="Unresolved")  # Status (e.g., Unresolved, In Progress, Resolved)
    assigned_to = db.Column(db.String(100), nullable=True)  # User responsible for fixing it
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Vulnerability {self.id} - {self.url}>'

@app.route('/vulnerabilities')
def vulnerabilities():
    vulnerabilities = Vulnerability.query.all()
    return render_template('vulnerabilities.html', vulnerabilities=vulnerabilities)

# add vulnerability
@app.route('/vulnerabilities/new', methods=['GET', 'POST'])
def new_vulnerability():
    if request.method == 'POST':
        url = request.form['url']
        description = request.form['description']
        status = request.form['status']
        new_vulnerability = Vulnerability(url=url, description=description, status=status)
        try:
            db.session.add(new_vulnerability)
            db.session.commit()
            flash('Vulnerability added successfully!')
            return redirect('/vulnerabilities')
        except:
            flash('There was an issue adding the vulnerability.')
    return render_template('new_vulnerability.html')

# update vulnerability
@app.route('/vulnerabilities/update/<int:id>', methods=['GET', 'POST'])
def update_vulnerability(id):
    vulnerability = Vulnerability.query.get_or_404(id)
    if request.method == 'POST':
        vulnerability.status = request.form['status']
        vulnerability.assigned_to = request.form['assigned_to']
        try:
            db.session.commit()
            flash('Vulnerability updated successfully!')
            return redirect('/vulnerabilities')
        except:
            flash('There was an issue updating the vulnerability.')
    return render_template('update_vulnerability.html', vulnerability=vulnerability)

# delete vulnerability
@app.route('/vulnerabilities/delete/<int:id>')
def delete_vulnerability(id):
    vulnerability = Vulnerability.query.get_or_404(id)
    try:
        db.session.delete(vulnerability)
        db.session.commit()
        flash('Vulnerability deleted successfully!')
        return redirect('/vulnerabilities')
    except:
        flash('There was an issue deleting the vulnerability.')

# login from ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# sign up
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists!')
            return redirect(url_for('signup'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()

        flash('User created successfully!')
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            flash('Login unsuccessful. Check username and password.')
            return redirect(url_for('login'))

        login_user(user)
        flash('Logged in successfully!')
        return redirect(url_for('dashboard'))

    return render_template('login.html')

#  protected Dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    reports = Report.query.filter_by(user_id=current_user.id).all()

    return render_template('dashboard.html', reports=reports)

# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('login'))

# admin
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.role != 'admin':
            flash('You do not have permission to access this page.')
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)

    return decorated_function

@app.route('/admin')
@login_required
@admin_required
def admin_dashboard():
    return "Welcome to the Admin Dashboard!"

# path to scan vulnerabilities
@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        url = request.form["url"]
        vulnerabilities = perform_scan(url)

        # save report in database
        report = Report(url=url, vulnerabilities=str(vulnerabilities), user_id=current_user.id)
        db.session.add(report)
        db.session.commit()

        # Get report in pdf format
        report_file = generate_report(vulnerabilities)

        # send report as downloadable file
        return send_file(report_file, as_attachment=True, download_name="security_report.pdf", mimetype='application/pdf')

    return render_template("index.html")

# Create tables in database (only one time)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
