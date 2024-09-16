import requests

'''
    Clickjacking is an attack that tricks a user into clicking a webpage element 
    which is invisible or disguised as another element. 
    This can cause users to unwittingly download malware.
'''
def test_clickjacking(url):
    headers = {"X-Frame-Options": "DENY"}
    response = requests.get(url, headers=headers)
    if "X-Frame-Options" not in response.headers:
        return {"vulnerability": "Clickjacking", "status": "Detected", "details": "X-Frame-Options header missing"}
    return {"vulnerability": "Clickjacking", "status": "Not detected", "details": "Page protected against clickjacking"}
