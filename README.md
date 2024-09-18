# Security-Scanner
This Security Scanner Application is designed to scan websites for various security vulnerabilities. The app performs multiple security checks, including testing for SQL Injection, XSS, CSRF, SSRF, and more, using multithreading for efficient parallel scanning. It is built using Python, Flask for the web interface, and several security testing tools and techniques.

# Features

+ User Authentication: User signup and login functionality with hashed password storage.

+ Role-Based Access Control: Different views based on user roles.
  
+ Vulnerability Scanning: Scans for a variety of web security vulnerabilities, including but not limited to:
  
    + SQL Injection
    + Cross-Site Scripting (XSS)
    + Directory Traversal
    + CSRF (Cross-Site Request Forgery)
    + SSRF (Server-Side Request Forgery)
    + Brute Force
    + Path Traversal
    + Command Injection
    + Security Headers (Content-Security Policy, X-Frame-Options, etc.)
    + File Upload Vulnerabilities
    + Open Redirects
    + HTML Injection
    + Insecure Cookies
    + Insecure HTTP Methods (Method Tampering)
    + CORS Misconfiguration
    + Clickjacking
    + Sensitive Data Exposure
    + Deserialization Vulnerabilities
+ Multithreading: Uses ThreadPoolExecutor to perform scans concurrently.
+ Result Dashboard: Displays user-specific reports with details on each vulnerability found.
+ Report Storage: Vulnerability reports are stored in the database and displayed in the user dashboard.
+ Extensible Framework: New vulnerability checks can easily be added.

# Technologies Used
- Backend
  
    + Python 3.x: Core programming language for logic and processing.
    + Flask: Micro web framework used to handle routing, rendering HTML templates, and managing user authentication.
    + Werkzeug: Library for password hashing and security utilities.
    + Concurrent.futures: For handling multithreading, enabling multiple vulnerability checks to be run in parallel.
    + Requests: Python library for making HTTP requests during the vulnerability checks.
      
- Database
  
    + SQLite: Lightweight database used for storing user data and reports.
      
- Frontend
  
    + HTML/CSS: For basic layout and design of the application.
      
- Security Libraries
  
    + OWASP ZAP API (Optional, not yet integrated): Can be used for advanced scanning.
    + Requests: To send requests and check the response for security vulnerabilities.
      
# Templates

1) admin_dashboard.html:

This template is for the admin view, where admins can manage all users, view their reports, and add or update vulnerabilities.

2) dashboard.html:

The user dashboard where regular users can see their vulnerability reports and initiate new scans.

3) index.html:

The homepage of the application. 

4) login.html:

This template provides the login form where users can enter their credentials.

5) new_vulnerability.html:

A form for admins to add a new vulnerability type to the system. This allows admins to extend the types of vulnerabilities the scanner can check.

6) signup.html:

A form for new users to register an account. Includes fields for username, password and role.

7) update_vulnerability.html:

Admins use this page to update details about existing vulnerabilities, such as descriptions or scan methods.

8) vulnerabilities.html:

This template lists all known vulnerabilities in the system, accessible to admins for managing them.

# Sample Application Screenshots

- homepage: it allows users to get a report without logging in (in a pdf format that automatically downloads after user presses 'scan')
  
  ![image](https://github.com/user-attachments/assets/b885916b-c7a2-459d-95d3-85d45db5c925)
  ![repo](https://github.com/user-attachments/assets/1e5a4308-5641-49cf-a9a9-b49bdd0c221c)

- signup
  
  ![image](https://github.com/user-attachments/assets/5c9405f3-5f7a-485b-bd8a-2c90ea341158)
- dashboard(after logging in)

  
  ![image](https://github.com/user-attachments/assets/d4bb61c3-2cfb-454f-b0d1-e97040314ada)
- vulnerabilities
  ![Screenshot 2024-09-15 212945](https://github.com/user-attachments/assets/a4f7900d-001b-4681-9279-c788e09a77c3)
  
- new vulnerability
  
  ![image](https://github.com/user-attachments/assets/e8de3392-9b40-44c4-965c-667ede883d58)

# Prerequisites

  - Python 3.x
  - Pip
  - SQLite3 (or any other database backend if configured)

# Usage

  - Signup/Login
      - Signup: Visit http://127.0.0.1:5000/signup to create an account.
      - Login: Once signed up, log in via http://127.0.0.1:5000/login.
        
  - Dashboard
      - Once logged in, you will be redirected to the dashboard where you can:
      - Enter a URL to scan for vulnerabilities.
      - View previously generated reports.
        
  - Admins can manage the vulnerabilities.
    
  - Running a Scan
      - Enter the URL you wish to scan into the input form on the dashboard.  
      - The backend will start scanning using multiple threads.
      - Once the scan is complete, the results are displayed and stored in the database.
        
  - Admin Features
      - Add New Vulnerabilities: Admins can add new types of vulnerabilities using the new_vulnerability.html form.
      - Update Vulnerabilities: Admins can update vulnerability details, such as payloads or detection methods, via update_vulnerability.html.
      - Remove Vulnerabilities: Admins can remove a vulnerability
       
## Troubleshooting

If you run into any problems, here are some common solutions:

- **Database Errors**:
  - Ensure that SQLite is properly initialized with `flask db init` and `flask db migrate`.

- **Dependencies Issues**:
  - Run `pip install -r requirements.txt` to make sure all dependencies are installed.

- **Scanning Issues**:
  - If vulnerability tests fail, ensure that the URLs you're testing are reachable and that the payloads are not blocked by firewalls or other network restrictions.

- **Permission Errors**:
  - Ensure that your Flask app has proper file access permissions, especially if you're running it on a Linux server.
   
## Security Considerations

- **User Passwords**: Passwords are hashed using secure hashing algorithms (e.g., SHA256).
 
- **Session Management**: Flask's session management is used to handle login and user sessions securely.
 
- **Database Security**: SQL queries use parameterized statements to prevent SQL injection in the application’s backend.
 
- **Vulnerability Output Handling**: Ensure that scan results are properly sanitized before being rendered in templates to prevent stored XSS.

    
# Extending the Application
The application is designed to be extensible. To add new vulnerability tests:
  - Create a new test function in the vulnerabilities/ directory.
  - Modify the main.py to call this function when scanning a URL.
  - Add a new template (if necessary) to handle any new views or input forms.
    
# Future Improvements
  - Asynchronous Scanning: Migrate to asynchronous scanning with asyncio for further performance improvements.
  - Real-time Alerts: Add real-time notifications for critical vulnerabilities.
  - More Detailed Reports: Add charts and graphs to visualize the results.
  - Admin Panel: Create an admin panel for viewing all user activity.

        
