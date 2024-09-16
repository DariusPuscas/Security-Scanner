import requests

'''
    File upload vulnerabilities are when a web server allows users to upload files to its filesystem 
    without sufficiently validating things like their name, type, contents, or size
'''
def test_file_upload(url):
    # upload malicious file
    file_data = {
        'file': ('malicious.php', '<?php echo "Malicious Code"; ?>')
    }
    response = requests.post(url, files=file_data)
    if response.status_code == 200:
        return {"vulnerability": "File Upload", "status": "Potential issue", "details": "Possible file upload vulnerability"}
    return {"vulnerability": "File Upload", "status": "No issue", "details": "No file upload vulnerability detected"}