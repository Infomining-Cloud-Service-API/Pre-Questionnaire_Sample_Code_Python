import requests, json
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from setting import constants

# ========== Step3 Scenario : Questions ==========
"""
    <parameters>
    url : /v1/step3/questions
    accessToken : OAuth2.0 accessToken (auth.py > getToken())
    language_type : 'kr', 'en'(None : 'en')
    report_id : identifier of report
"""
def questions(url, accessToken, language_type, report_id):
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        params = {
            'language_type': language_type,
            'report_id': report_id,
        }
        response = requests.get(url, headers=headers, params=params)

        print("questions response code : {0}".format(response.status_code))
        print("questions response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("questions error : {0}".format(e))

# ========== Step3 Scenario : Question ==========
"""
    <parameters>
    url : /v1/step3/question
    accessToken : OAuth2.0 accessToken (auth.py > getToken())
    language_type : 'kr', 'en'(None : 'en')
    question_id : identifier of question
    report_id : identifier of report
"""
def question(url, accessToken, language_type, question_id, report_id):
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        params = {
            'language_type': language_type,
            'question_id': question_id,
            'report_id': report_id,
        }
        response = requests.get(url, headers=headers, params=params)

        print("question response code : {0}".format(response.status_code))
        print("question response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("question error : {0}".format(e))

# ========== Step3 Scenario : Follow Up ==========
"""
    <parameters>
    url : /v1/step3/followUp
    accessToken : OAuth2.0 accessToken (auth.py > getToken())
    language_type : 'kr', 'en'(None : 'en')
    follow_up_id : Step3 Additional Question Identifiers for Questions
"""
def followUp(url, accessToken, language_type, follow_up_id):
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        params = {
            'language_type': language_type,
            'follow_up_id': follow_up_id,
        }
        response = requests.get(url, headers=headers, params=params)

        print("followUp response code : {0}".format(response.status_code))
        print("followUp response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("followUp error : {0}".format(e))

# ========== Step3 Scenario : Save Step3 Report ==========
"""
    <parameters>
    url : /v1/report/step3/saveReport
    accessToken : OAuth2.0 accessToken (auth.py > getToken())
    report_id : identifier of report
    question_id : identifier of question
    followup_question_id : Identifier of followup question
    selection_id : identifier of Step3 Selection 
    input_txt : Answers to subjective questions
    question_type : Type of question to save(objective, subjective, mixed, follow_up)
"""
def saveStep3Report(url, accessToken, report_id, question_id, followup_question_id, selection_id, input_txt, question_type):
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        params = {
            'report_id': report_id,
            'question_type': question_type,
        }
        if question_id:
            params['question_id']=question_id
        if followup_question_id:
            params['followup_question_id']=followup_question_id
        if selection_id:
            params['selection_id']=selection_id
        if input_txt:
            params['input_txt']=input_txt

        response = requests.post(url, headers=headers, params=params)

        print("saveStep3Report response code : {0}".format(response.status_code))
        print("saveStep3Report response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("saveStep3Report error : {0}".format(e))

# ========== Step3 Scenario : Step3 History ==========
"""
    <parameters>
    url : /v1/report/step3/history
    accessToken : OAuth2.0 accessToken (auth.py > getToken())
    report_id : identifier of report
"""
def step3History(url, accessToken, report_id):
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        params = {
            'report_id': report_id,
        }
        response = requests.get(url, headers=headers, params=params)

        print("step3History response code : {0}".format(response.status_code))
        print("step3History response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("step3History error : {0}".format(e))

# ========== Step3 Scenario : Report End ==========
"""
    <parameters>
    url : /v1/report/reportEnd
    accessToken : OAuth2.0 accessToken (auth.py > getToken())
    report_id : identifier of report
"""
def reportEnd(url, accessToken, report_id):
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        params = {
            'report_id': report_id,
        }
        response = requests.post(url, headers=headers, params=params)

        print("reportEnd response code : {0}".format(response.status_code))
        print("reportEnd response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("reportEnd error : {0}".format(e))


if __name__ == '__main__' :
    print('start')
    # questions(
    #     url= constants.apiUrl + '/v1/step3/questions',
    #     accessToken=constants.accessToken,
    #     language_type='kr',
    #     report_id=constants.reportId,
    # )
    # question(
    #     url= constants.apiUrl + '/v1/step3/question',
    #     accessToken=constants.accessToken,
    #     language_type='kr',
    #     question_id=constants.step3_question_id,
    #     report_id=constants.reportId,
    # )
    # followUp(
    #     url= constants.apiUrl + '/v1/step3/followUp',
    #     accessToken=constants.accessToken,
    #     language_type='kr',
    #     follow_up_id=constants.follow_up_id,
    # )
    # saveStep3Report(
    #     url= constants.apiUrl + '/v1/report/step3/saveReport',
    #     accessToken=constants.accessToken,
    #     report_id=constants.reportId,
    #     question_id=constants.step3_question_id,
    #     followup_question_id=constants.followup_question_id,
    #     selection_id=constants.step3_selection_id,
    #     input_txt=None,
    #     question_type='objective',
    # )
    # step3History(
    #     url= constants.apiUrl + '/v1/report/step3/history',
    #     accessToken=constants.accessToken,
    #     report_id=constants.reportId,
    # )
    # reportEnd(
    #     url= constants.apiUrl + '/v1/report/reportEnd',
    #     accessToken=constants.accessToken,
    #     report_id=constants.reportId,
    # )