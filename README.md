# INFOMINING API REFERENCE - Python
  InfoMining API Reference for Python

# Getting Started
### Install Package
```python
> pip install -r requirements.txt
```

# File Structure
**Each EndPoint can be referenced through functions within the corresponding file.**

- api
    - auth.py
    - get_report.py
    - preparation_scenario.py
    - step1_scenario.py
    - step2_scenario.py
    - step3_scenario.py
    - symptom_selection.py

- extension(not using)

- setting
  - constants.py (variables to test)
  
* requirements.txt (package infomations)

# OAuth 2.0

**AccessToken** is required to use InfoMining's API.

The token can be issued through a getToken function call in the file **'auth.py'**.

```python
# ========== Issuing tokens  ==========
def getToken(url, projectId, projectSecret):
    # url : /v1/auth/token
    # projectId : project ID
    # proejctSecret : project secret key
    try:
        headers = {
            'Project-Id': projectId,
            'Project-Secret': projectSecret,
        }
        response = requests.post(url, headers=headers)

        print("getToken response code : {0}".format(response.status_code))
        print("getToken response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("getToken error : {0}".format(e))
```
