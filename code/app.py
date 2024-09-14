from flask import Flask, render_template, request, send_file
from main import perform_scan  # scan
from reports.generate_report import generate_report

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = True  # Util for HTTPS

app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.after_request
def set_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        vulnerabilities = perform_scan(url)

        # Generate report
        report_file = generate_report(vulnerabilities)

        # send and download
        return send_file(report_file, as_attachment=True, download_name="security_report.pdf",
                         mimetype='application/pdf')

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
