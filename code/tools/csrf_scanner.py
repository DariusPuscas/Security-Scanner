import requests

def test_csrf(url):
    proxies = {
        "http": None,
        "https": None,
    }
    response = requests.get(url, proxies=proxies)
    if 'csrf_token' not in response.text:
        return "CSRF vulnerability detected"
    return "No CSRF vulnerability found"