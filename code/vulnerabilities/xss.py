import requests
def test_xss(url, param):
    xss_payload = "<script>alert('XSS')</script>"
    test_url = f"{url}?{param}={xss_payload}"

    try:
        response = requests.get(test_url)
        if xss_payload in response.text:
            return f"Possible XSS vulnerability at {test_url}"
        else:
            return f"No XSS vulnerability found at {test_url}"
    except Exception as e:
        return f"Error testing XSS: {e}"


# Example Usage
#print(test_xss("http://example.com/search", "query"))
