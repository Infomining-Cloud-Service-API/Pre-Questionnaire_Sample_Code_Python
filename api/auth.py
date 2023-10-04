import requests, json
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from setting import constants

# ========== Issuing tokens  ==========
def getToken(url, projectId, projectSecret):
    # url : /v1/auth/token
    # projectId : project ID
    # proejctSecret : project secret key
    try:
        headers = {
            'Project-Id': projectId,
            'Project-Secret': projectSecret,
            'Content-Type': constants.ContentType,
        }
        response = requests.post(url, headers=headers)

        print("getToken response code : {0}".format(response.status_code))
        print("getToken response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("getToken error : {0}".format(e))

# ========== Token reissuance  ==========
def getRefreshToken(url, refreshToken):
    # url : /v1/auth/refresh_token
    # refreshToken : refreshToken
    try:
        headers = {
            'Refresh-Token': refreshToken,
            'Content-Type': constants.ContentType,
        }
        response = requests.post(url, headers=headers)

        print("getRefreshToken response code : {0}".format(response.status_code))
        print("getRefreshToken response data : {0}".format(response.text))
        
        return response
    except Exception as e:
        print("getRefreshToken error : {0}".format(e))


if __name__ == '__main__' :
    print('start')
    getToken(
        url= constants.authUrl + '/v1/auth/token', 
        projectId='test_prj-wtM795110', 
        projectSecret='YgvrukdGQO8Gu6IH4ZH7SfVvZHaemeqT'
    )
    #
    # getRefreshToken(
    #     url= constants.authUrl + '/v1/auth/refresh_token', 
    #     refreshToken='5HsQtMBtA4z8dufTUxZ9uwUj1HhkeGVz+X1t0kptS/NeajItPRACPdQRtbxtqj34xqNSV+lhBTJfxQMlvMI/m8Cln7OmvueqnLCxLMiAxP81', 
    # )