import requests

'''
    Insecure HTTPS cookies are those transmitted over unencrypted connections, 
    making them vulnerable to interception by malicious actors. 
    Unlike their secure counterparts, these cookies lack encryption, 
    exposing sensitive information to potential attacks.
'''

def test_insecure_cookies(url):
    response = requests.get(url)
    cookies = response.cookies
    insecure_cookies = []
    for cookie in cookies:
        if not cookie.secure or not cookie.has_nonstandard_attr('HttpOnly'):
            insecure_cookies.append(cookie.name)
    if insecure_cookies:
        return {"vulnerability": "Insecure Cookies", "status": "Detected", "details": f"Insecure cookies found: {', '.join(insecure_cookies)}"}
    return {"vulnerability": "Insecure Cookies", "status": "Not detected", "details": "All cookies are secure"}