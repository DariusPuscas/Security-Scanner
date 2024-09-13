import argparse
from reports.generate_report import generate_report
from vulnerabilities.sql_injection import test_sql_injection
from vulnerabilities.xss import test_xss
from vulnerabilities.directory_traversal import test_directory_traversal
from tools.owasp_zap import scan_with_zap
from tools.csrf_scanner import test_csrf
from tools.brute_force import test_brute_force
import concurrent.futures

def main():
    parser = argparse.ArgumentParser(description="Web Security Scanner Tool")
    parser.add_argument("url", help="Target URL to scan")
    args = parser.parse_args()

    # Perform scans concurrently
    vulnerabilities = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(test_sql_injection, args.url, "param"),
            executor.submit(test_xss, args.url, "param"),
            executor.submit(test_directory_traversal, args.url, "param"),
            executor.submit(test_csrf, args.url),
            executor.submit(test_brute_force, args.url),
           # executor.submit(scan_with_zap, args.url)
        ]
        vulnerabilities = [f.result() for f in concurrent.futures.as_completed(futures)]

    # Generate report
   # generate_report(vulnerabilities)

if __name__ == "__main__":
    main()