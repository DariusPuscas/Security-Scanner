import requests

'''
    Method tampering (aka verb tampering and HTTP method tampering) is an attack against authentication
    or authorization systems that have implicit "allow all" settings in their security configuration
'''

def test_http_methods(url):
    methods = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
    insecure_methods = []
    for method in methods:
        response = requests.request(method, url)
        if response.status_code == 200:
            insecure_methods.append(method)
    if insecure_methods:
        return {"vulnerability": "HTTP Method Tampering", "status": "Detected", "details": f"Insecure methods detected: {', '.join(insecure_methods)}"}
    return {"vulnerability": "HTTP Method Tampering", "status": "Not detected", "details": "No insecure HTTP methods found"}