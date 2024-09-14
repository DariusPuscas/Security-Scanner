import requests

def test_security_headers(url):
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        missing_headers = []

        if "Strict-Transport-Security" not in headers:
            missing_headers.append("Strict-Transport-Security")

        if "X-Frame-Options" not in headers:
            missing_headers.append("X-Frame-Options")

        if "Content-Security-Policy" not in headers:
            missing_headers.append("Content-Security-Policy")

        if "X-XSS-Protection" not in headers:
            missing_headers.append("X-XSS-Protection")

        if missing_headers:
            return {"vulnerability": "Security Headers", "status": "Detected",
                    "details": f"Missing headers: {', '.join(missing_headers)}"}

    except requests.exceptions.RequestException as e:
        pass
    return {"vulnerability": "Security Headers", "status": "Not detected"}