import requests, json
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from setting import constants

# ========== Get Report : Get Summary Report info ==========
"""
    <parameters>
    url : /v1/report/get_summary_report_info
    accessToken : OAuth2.0 accessToken (auth.py > getToken())
    report_id : identifier of report
    report_type : type of report(report, question)
"""
def getSummaryReportInfo(url, accessToken, report_id, report_type):
    try:
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': constants.ContentType,
        }
        params = {
            'report_id': report_id,
            'report_type': report_type,
        }
        response = requests.get(url, headers=headers, params=params)

        print("getSummaryReportInfo response code : {0}".format(response.status_code))
        print("getSummaryReportInfo response data : {0}".format(response.text))

        return response
    except Exception as e:
        print("getSummaryReportInfo error : {0}".format(e))



if __name__ == '__main__' :
    print('start')
    # getSummaryReportInfo(
    #     url= constants.apiUrl + '/v1/report/get_summary_report_info',
    #     accessToken=constants.accessToken,
    #     report_id=constants.reportId,
    #     report_type=constants.report_type,
    # )