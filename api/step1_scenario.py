import requests, json
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from setting import constants

# ========== Step1 Scenario : Get Questions ==========
def step1GetQuestions(url, accessToken, language_type):
    # url : /v1/step1/questions
    # language_type : 'kr', 'en'(None : 'en')
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        params = {
            'language_type': language_type,
        }
        response = requests.post(url, headers=headers, params=params)

        print("step1GetQuestions response code : {0}".format(response.status_code))
        print("step1GetQuestions response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("step1GetQuestions error : {0}".format(e))

# ========== Step1 Scenario : Get Question Only One ==========
def step1GetQuestion(url, accessToken, language_type, question_id):
    # url : /v1/step1/question
    # language_type : 'kr', 'en'(None : 'en')
    # question_id : identifier of step1 question
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        params = {
            'language_type': language_type,
            'question_id': question_id,
        }
        response = requests.post(url, headers=headers, params=params)

        print("step1GetQuestion response code : {0}".format(response.status_code))
        print("step1GetQuestion response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("step1GetQuestion error : {0}".format(e))

# ========== Step1 Scenario : Save Step1 Report ==========
def saveStep1Report(url, accessToken, report_id, question_id, selection_id, input_txt):
    # url : /v1/report/step1/saveReport
    # report_id : identifier of report
    # question_id : identifier of Step1 question
    # selection_id : identifier of Step1 Selection 
    # input_txt : Content of Step1 Selection (Exists only when subjective)
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        params = {
            'report_id':report_id,
            'question_id':question_id,
            'selection_id':selection_id,
        }
        if(input_txt):
            params['input_txt']:input_txt
        print(params)
        response = requests.post(url, headers=headers, params=params)

        print("saveStep1Report response code : {0}".format(response.status_code))
        print("saveStep1Report response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("saveStep1Report error : {0}".format(e))

# ========== Step1 Scenario : Save Step1 User Info ==========
"""
    <parameters>
    url : /v1/report/step1/saveReportUserInfo
    report_id : identifier of report
    user_age : Age of user
    user_height : Height of user
    user_weight : Weight of use
"""
def saveStep1UserInfo(url, accessToken, report_id, user_age, user_height, user_weight):
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        params = {
            'report_id':report_id,
            'user_age':user_age,
            'user_height':user_height,
            'user_weight':user_weight,
        }
        print(params)
        response = requests.post(url, headers=headers, params=params)

        print("saveStep1UserInfo response code : {0}".format(response.status_code))
        print("saveStep1UserInfo response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("saveStep1UserInfo error : {0}".format(e))

# ========== Step1 Scenario : Step1 History ==========
def step1History(url, accessToken, report_id):
    # url : /v1/report/step1/history
    # report_id : identifier of report
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        params = {
            'report_id':report_id,
        }
        response = requests.get(url, headers=headers, params=params)

        print("step1History response code : {0}".format(response.status_code))
        print("step1History response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("step1History error : {0}".format(e))

if __name__ == '__main__' :
    print('start')
    # step1GetQuestions(
    #     url= constants.apiUrl + '/v1/step1/questions',
    #     accessToken=constants.accessToken,
    #     language_type='en',
    # )
    # step1GetQuestion(
    #     url= constants.apiUrl + '/v1/step1/question',
    #     accessToken=constants.accessToken,
    #     language_type='kr',
    #     question_id='base001',
    # )
    # saveStep1Report(
    #     url= constants.apiUrl + '/v1/report/step1/saveReport',
    #     accessToken=constants.accessToken,
    #     report_id=constants.reportId,
    #     question_id='base001',
    #     selection_id='sbase000',
    #     input_txt='test',
    # )
    # saveStep1UserInfo(
    #     url= constants.apiUrl + '/v1/report/step1/saveReportUserInfo',
    #     accessToken=constants.accessToken,
    #     report_id=constants.reportId,
    #     user_age='27',
    #     user_height='180',
    #     user_weight='70',
    # )
    # step1History(
    #     url= constants.apiUrl + '/v1/report/step1/history',
    #     accessToken=constants.accessToken,
    #     report_id=constants.reportId,
    # )