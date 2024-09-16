import requests

'''
    HTML injection is a type of attack where malicious HTML code is inserted into a website
'''
def test_html_injection(url, param):
    payload = "<h1>Injected HTML</h1>"
    test_url = f"{url}?{param}={payload}"
    response = requests.get(test_url)
    if "<h1>Injected HTML</h1>" in response.text:
        return {"vulnerability": "HTML Injection", "status": "Detected", "details": f"HTML injection vulnerability found at {test_url}"}
    return {"vulnerability": "HTML Injection", "status": "Not detected", "details": "No HTML injection vulnerability detected"}
