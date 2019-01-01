# coding=utf-8

import os
import time


def CreateHtmlTestReport(testMode, reportPath, reportName):
    """
    创建测试报告的方法
    :param testMode:
    :param reportPath: 格式：'/my/path/'
    :param reportName:
    :return:
    """
    # reportDate = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    reportCreateTime = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
    reportSavePath = os.getcwd() + reportPath
    reportType = u'.html'
    if testMode == u'mb':
        fp = reportSavePath + reportCreateTime
        if os.path.exists(fp):
            myPath = fp + '/' + reportName + reportType
            return myPath
        else:
            os.mkdir(fp)
            myPath = fp + '/' + reportName + reportType
            return myPath
    elif testMode == u'cs':
        fp = reportSavePath + reportCreateTime
        if os.path.exists(fp):
            myPath = fp + '/' + reportName + reportType
            return myPath
        else:
            os.mkdir(fp)
            myPath = fp + '/' + reportName + reportType
            return myPath
