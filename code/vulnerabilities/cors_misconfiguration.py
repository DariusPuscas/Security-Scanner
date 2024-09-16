import requests

'''
    A CORS misconfiguration occurs when a web application's CORS policy is incorrectly configured, 
    allowing unauthorized domains to access its resources.
'''
def test_cors_misconfiguration(url):
    response = requests.options(url, headers={"Origin": "https://malicious.com"})
    if "Access-Control-Allow-Origin" in response.headers and response.headers["Access-Control-Allow-Origin"] == "*":
        return {"vulnerability": "CORS Misconfiguration", "status": "Detected", "details": "CORS policy allows all origins"}
    return {"vulnerability": "CORS Misconfiguration", "status": "Not detected", "details": "CORS policy is safe"}




