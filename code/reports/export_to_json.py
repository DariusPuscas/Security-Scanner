import json

def export_to_json(vulnerabilities, filename="report.json"):
    with open(filename, 'w') as f:
        json.dump(vulnerabilities, f)
    print(f"JSON report saved as {filename}")