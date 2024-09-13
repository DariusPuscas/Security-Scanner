import requests

def test_brute_force(url):

    login_data = {'username': 'admin', 'password': 'wrongpassword'}
    for i in range(10):  # Simulate multiple login attempts
        response = requests.post(url, data=login_data)
        if "blocked" in response.text:
            return "Brute-force protection enabled"
    return "No brute-force protection found"