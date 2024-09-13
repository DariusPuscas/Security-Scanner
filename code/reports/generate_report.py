import pdfkit

# Define the path to wkhtmltopdf manually if needed
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
def generate_report(vulnerabilities, filename="report.pdf"):
    # Implementation to generate a PDF report
    html_content = "<h1>Security Vulnerability Report</h1>"

    for vuln in vulnerabilities:
        html_content += f"<p>{vuln}</p>"

    # Saving the report as a PDF file
    pdfkit.from_string(html_content, filename)
    print(f"Report saved as {filename}")

#def generate_report(vulnerabilities, filename="report.pdf"):
#    html_content = "<h1>Security Vulnerability Report</h1>"
#
#   for vuln in vulnerabilities:
 #       severity = "High" if "Vulnerability Found" in vuln else "Low"
 #       html_content += f"<p>Vulnerability: {vuln} | Severity: {severity}</p>"

    # Generate PDF
   # pdfkit.from_string(html_content, filename)
  #  print(f"Report saved as {filename}")