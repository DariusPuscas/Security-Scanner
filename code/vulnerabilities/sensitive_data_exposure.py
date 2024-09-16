import requests

'''
    A sensitive data exposure occurs when sensitive information is inadvertently disclosed
    or made accessible to unauthorized individuals or entities. 
    This exposure can happen due to various factors. These include misconfigured systems, human error,
    or inadequate security measures. Data exposure is typically unintentional.
'''
def test_sensitive_data_exposure(url):
    response = requests.get(url)
    if response.url.startswith("http://"):
        return {"vulnerability": "Sensitive Data Exposure", "status": "Detected", "details": "Connection is not secure (HTTPS not used)"}
    return {"vulnerability": "Sensitive Data Exposure", "status": "Not detected", "details": "Connection is secure"}
