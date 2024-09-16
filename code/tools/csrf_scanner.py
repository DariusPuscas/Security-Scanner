import requests

'''
    Cross-Site Request Forgery (CSRF) is an attack that forces authenticated users 
    to submit a request to a Web application against which they are currently authenticated.
    CSRF attacks exploit the trust a Web application has in an authenticated user
'''
def test_csrf(url):
    proxies = {
        "http": None,
        "https": None,
    }
    response = requests.get(url, proxies=proxies)
    if 'csrf_token' not in response.text:
        return "CSRF vulnerability detected"
    return "No CSRF vulnerability found"