import requests

'''
A Server-Side Request Forgery (SSRF) attack involves an attacker abusing server functionality
to access or modify resources. The attacker targets an application that supports data imports 
from URLs or allows them to read data from URLs
'''
def test_ssrf(url):
    ssrf_test_urls = [
        "http://127.0.0.1",
        "http://169.254.169.254",  # AWS metadata service, indicator for     SSRF
        "http://localhost",
        "http://0.0.0.0"
    ]

    for test_url in ssrf_test_urls:
        try:
            response = requests.get(url, params={'url': test_url}, timeout=5)
            if response.status_code == 200:
                return {"vulnerability": "SSRF", "status": "Detected", "details": f"URL {test_url} was accessible"}
        except requests.exceptions.RequestException as e:
            pass
    return {"vulnerability": "SSRF", "status": "Not detected"}