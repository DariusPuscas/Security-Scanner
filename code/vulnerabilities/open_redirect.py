import requests

'''
    An Open Redirect is a vulnerability
    in a web application that allows an attacker to redirect a user to an arbitrary website
'''
def test_open_redirect(url, param):
    payload = "https://malicious.com"
    test_url = f"{url}?{param}={payload}"
    response = requests.get(test_url, allow_redirects=False)
    if response.status_code in [301, 302] and "https://malicious.com" in response.headers.get("Location", ""):
        return {"vulnerability": "Open Redirect", "status": "Detected", "details": f"Open redirect vulnerability found at {test_url}"}
    return {"vulnerability": "Open Redirect", "status": "Not detected", "details": "No open redirect vulnerability detected"}