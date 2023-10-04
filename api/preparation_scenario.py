import requests, json
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from setting import constants

# ========== Generating initial report ==========
def reportStart(url, accessToken):
    # url : /v1/report/reportStart
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        response = requests.post(url, headers=headers)

        print("reportStart response code : {0}".format(response.status_code))
        print("reportStart response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("reportStart error : {0}".format(e))

# ========== Step1 Save Report ==========
def saveReportTotal(url, accessToken, user_name, user_gender, user_age, user_pregnant, user_height, user_weight, user_job, user_religion):
    # url : /v1/report/step1/saveReportTotal
    # required : user_name, user_gender, user_age
    # non-required : user_pregnant(NULL=not pregant), user_height, user_weight, user_job, user_religion
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        params = {
            'user_name':user_name,
            'user_gender':user_gender,
            'user_age':user_age,
        }
        if user_pregnant:
            params['user_pregnant']=user_pregnant
        if user_height:
            params['user_height']=user_height
        if user_weight:
            params['user_weight']=user_weight
        if user_job:
            params['user_job']=user_job
        if user_religion:
            params['user_religion']=user_religion
        response = requests.post(url, headers=headers, params=params)

        print("saveReportTotal response code : {0}".format(response.status_code))
        print("saveReportTotal response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("saveReportTotal error : {0}".format(e))

if __name__ == '__main__' :
    print('start')
    reportStart(
        url= constants.apiUrl + '/v1/report/reportStart',
        accessToken=constants.accessToken,
    )
    #
    # saveReportTotal(
    #     url= constants.apiUrl + '/v1/report/step1/saveReportTotal',
    #     accessToken=constants.accessToken,
    #     user_name='pythonTest',
    #     user_gender='M',
    #     user_age=1,
    #     # user_pregnant=None,
    #     # user_height=None,
    #     # user_weight=None,
    #     # user_job=None,
    #     # user_religion=None,
    #     #
    #     # user_pregnant='pregnant',
    #     # user_height=1,
    #     # user_weight=1,
    #     # user_job='testJob',
    #     # user_religion='testReligion',
    # )