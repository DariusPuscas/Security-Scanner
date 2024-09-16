
import concurrent.futures
from vulnerabilities.sql_injection import test_sql_injection
from vulnerabilities.xss import test_xss
from vulnerabilities.directory_traversal import test_directory_traversal
from tools.owasp_zap import scan_with_zap
from tools.csrf_scanner import test_csrf
from tools.brute_force import test_brute_force
from reports.generate_report import generate_report

from vulnerabilities.ssrf import test_ssrf
from vulnerabilities.path_traversal import test_path_traversal
from vulnerabilities.command_injection import test_command_injection
from vulnerabilities.security_headers import test_security_headers

from vulnerabilities.file_upload import test_file_upload
from vulnerabilities.html_injection import test_html_injection
from vulnerabilities.open_redirect import test_open_redirect
from vulnerabilities.clickjacking import test_clickjacking
from vulnerabilities.http_method_tampering import test_http_methods
from vulnerabilities.insecure_cookies import test_insecure_cookies
from vulnerabilities.insecure_deserialization import test_insecure_deserialization
from vulnerabilities.sensitive_data_exposure import test_sensitive_data_exposure
from vulnerabilities.cors_misconfiguration import test_cors_misconfiguration

# scan function
def perform_scan(url):
    #vulnerabilities = ["No issues"]

    # scans
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(test_sql_injection, url, "param"),
            executor.submit(test_xss, url, "param"),
            executor.submit(test_directory_traversal, url, "param"),
            executor.submit(test_csrf, url),
            executor.submit(test_brute_force, url),
            # executor.submit(scan_with_zap, url)
            executor.submit(test_ssrf, url),
            executor.submit(test_path_traversal, url),
            executor.submit(test_command_injection, url),
            executor.submit(test_security_headers, url),
            executor.submit(test_file_upload, url), # test
            executor.submit(test_html_injection, url, "param"),
            executor.submit(test_open_redirect, url, "param"),
            executor.submit(test_clickjacking, url),
            executor.submit(test_http_methods, url),
            executor.submit(test_insecure_cookies, url),
            executor.submit(test_insecure_deserialization, url),
            executor.submit(test_sensitive_data_exposure, url),
            executor.submit(test_cors_misconfiguration, url)
        ]
        #takes vulnerabilities
        vulnerabilities = [f.result() for f in concurrent.futures.as_completed(futures)]

    # Generate report

    return vulnerabilities
