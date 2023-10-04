import requests, json
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from setting import constants

# ========== Symptom Selection : Symptoms ==========
def symptoms(url, accessToken, language_type, report_id, param):
    # url : /v1/symptom/symptoms
    # language_type : 'kr', 'en'(None : 'en')
    # report_id : identifier of report
    # param : search keyword
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        params = {
            'language_type': language_type,
            'report_id': report_id,
            'param': param,
        }
        response = requests.get(url, headers=headers, params=params)

        print("symptoms response code : {0}".format(response.status_code))
        print("symptoms response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("symptoms error : {0}".format(e))

# ========== Symptom Selection : ML Symptoms ==========
def mlSymptoms(url, accessToken, language_type, report_id, param):
    # url : /v1/symptom/MLsymptoms
    # language_type : 'kr', 'en'(None : 'en')
    # report_id : identifier of report
    # param : search keyword
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        params = {
            'language_type': language_type,
            'report_id': report_id,
            'param': param,
        }
        response = requests.get(url, headers=headers, params=params)

        print("mlSymptoms response code : {0}".format(response.status_code))
        print("mlSymptoms response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("mlSymptoms error : {0}".format(e))

if __name__ == '__main__' :
    print('start')
    # symptoms(
    #     url= constants.apiUrl + '/v1/symptom/symptoms',
    #     accessToken=constants.accessToken,
    #     language_type='kr',
    #     report_id=constants.reportId,
    #     param='배가',
    # )
    mlSymptoms(
        url= constants.apiUrl + '/v1/symptom/MLsymptoms',
        accessToken=constants.accessToken,
        language_type='kr',
        report_id=constants.reportId,
        param='배가',
    )