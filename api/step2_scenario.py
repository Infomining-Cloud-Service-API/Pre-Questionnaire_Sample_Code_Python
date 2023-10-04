import requests, json
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from setting import constants

# ========== Step2 Scenario : Symptom Select ==========
def symptomSelect(url, accessToken, report_id, symptom_id):
    # url : /v1/report/step2/symptomSelect
    # report_id : identifier of report
    # symptom_id : identifier of symptom
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        params = {
            'report_id': report_id,
            'symptom_id': symptom_id,
        }
        response = requests.post(url, headers=headers, params=params)

        print("symptomSelect response code : {0}".format(response.status_code))
        print("symptomSelect response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("symptomSelect error : {0}".format(e))

# ========== Step2 Scenario : Departments ==========
def departments(url, accessToken, language_type, report_id):
    # url : /v1/step2/departments
    # language_type : 'kr', 'en'(None : 'en')
    # report_id : identifier of report
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

        print("departments response code : {0}".format(response.status_code))
        print("departments response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("departments error : {0}".format(e))

# ========== Step2 Scenario : Questions ==========
def questions(url, accessToken, language_type, symptom_id):
    # url : /v1/step2/questions
    # language_type : 'kr', 'en'(None : 'en')
    # symptom_id : identifier of symptom
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        params = {
            'language_type': language_type,
            'symptom_id': symptom_id,
        }
        response = requests.get(url, headers=headers, params=params)

        print("questions response code : {0}".format(response.status_code))
        print("questions response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("questions error : {0}".format(e))

# ========== Step2 Scenario : Question ==========
def question(url, accessToken, language_type, question_id, report_id):
    # url : /v1/step2/question
    # language_type : 'kr', 'en'(None : 'en')
    # question_id : identifier of question
    # report_id : identifier of report
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

# ========== Step2 Scenario : Branch Question ==========
def branchQuestion(url, accessToken, language_type, selection_id):
    # url : /v1/step2/question
    # language_type : 'kr', 'en'(None : 'en')
    # selection_id : identifier of Step2 Selection 
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        params = {
            'language_type': language_type,
            'selection_id': selection_id,
        }
        response = requests.get(url, headers=headers, params=params)

        print("branchQuestion response code : {0}".format(response.status_code))
        print("branchQuestion response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("branchQuestion error : {0}".format(e))

# ========== Step2 Scenario : Save Step2 Report ==========
def saveStep2Report(url, accessToken, report_id, question_id, selection_id, input_txt, question_type):
    # url : /v1/report/step2/saveReport
    # report_id : identifier of report
    # question_id : identifier of question
    # selection_id : identifier of Step2 Selection 
    # input_txt : Answers to subjective questions
    # question_type : Type of question to save(objective)
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        params = {
            'report_id': report_id,
            'question_id': question_id,
            'question_type': question_type,
        }
        if selection_id:
            params['selection_id']=selection_id
        if input_txt:
            params['input_txt']=input_txt

        response = requests.post(url, headers=headers, params=params)

        print("saveStep2Report response code : {0}".format(response.status_code))
        print("saveStep2Report response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("saveStep2Report error : {0}".format(e))

# ========== Step2 Scenario : Step2 History ==========
def step2History(url, accessToken, report_id):
    # url : /v1/report/step2/history
    # report_id : identifier of report
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        params = {
            'report_id': report_id,
        }
        response = requests.get(url, headers=headers, params=params)

        print("step2History response code : {0}".format(response.status_code))
        print("step2History response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("step2History error : {0}".format(e))

if __name__ == '__main__' :
    print('start')
    # symptomSelect(
    #     url= constants.apiUrl + '/v1/report/step2/symptomSelect',
    #     accessToken=constants.accessToken,
    #     report_id=constants.reportId,
    #     symptom_id=constants.symptom_id,
    # )
    # departments(
    #     url= constants.apiUrl + '/v1/step2/departments',
    #     accessToken=constants.accessToken,
    #     language_type='kr',
    #     report_id=constants.reportId,
    # )
    # questions(
    #     url= constants.apiUrl + '/v1/step2/questions',
    #     accessToken=constants.accessToken,
    #     language_type='kr',
    #     symptom_id=constants.symptom_id,
    # )
    # question(
    #     url= constants.apiUrl + '/v1/step2/question',
    #     accessToken=constants.accessToken,
    #     language_type='kr',
    #     question_id=constants.question_id,
    #     report_id=constants.reportId,
    # )
    # branchQuestion(
    #     url= constants.apiUrl + '/v1/step2/branchQuestion',
    #     accessToken=constants.accessToken,
    #     language_type='kr',
    #     selection_id=constants.selection_id,
    # )
    # saveStep2Report(
    #     url= constants.apiUrl + '/v1/report/step2/saveReport',
    #     accessToken=constants.accessToken,
    #     report_id=constants.reportId,
    #     question_id=constants.step2_question_id,
    #     selection_id=constants.step2_selection_id,
    #     input_txt=None,
    #     question_type='objective',
    # )
    # step2History(
    #     url= constants.apiUrl + '/v1/report/step2/history',
    #     accessToken=constants.accessToken,
    #     report_id=constants.reportId,
    # )