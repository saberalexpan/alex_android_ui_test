# coding=utf-8

import HTMLTestRunner_Chart
import Email
import CaseContainer
import CreateReport
import os
import time


if __name__ == '__main__':
    TestReport = open(CreateReport.CreateHtmlTestReport(u'mb', '/Report/MB/container_1/', 'MbUiTestForXIAOMI'), 'wb')
    runCase = HTMLTestRunner_Chart.HTMLTestRunner(
        title=u'测试容器_1',
        description="",
        stream=TestReport,
        verbosity=2,
        retry=3,
        save_last_try=True
    )
    runCase.run(CaseContainer.container_1)

    TestReport.close()

    """localTime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    LeastReport = Email.latest_report(os.getcwd() + '/Report/MB/container_1/')"""

    newReportSavePath = Email.NewReportPath(os.getcwd() + '/Report/MB/container_1/')
    LeastReport = Email.FindHtmlReport(newReportSavePath)
    Email.send_email(LeastReport)
