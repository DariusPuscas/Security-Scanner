import pdfkit

# Define the path to wkhtmltopdf manually if needed
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

def generate_report(vulnerabilities, filename="report.pdf"):
    # html report
    html_content = "<h1>Security Vulnerability Report</h1>"

    for vuln in vulnerabilities:
        severity = "High" if "SQL Injection" in vuln else "Low"
        html_content += f"<p>Vulnerability: {vuln} | Severity: {severity}</p>"

    # Save report as pdf file
    try:
        pdfkit.from_string(html_content, filename, configuration=config)
        print(f"Report saved as {filename}")
        return filename  # return file path
    except Exception as e:
        print(f"Error generating report: {e}")
        return None
