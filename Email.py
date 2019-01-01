# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import logging
import os


def send_email(report):
    read_report = open(report, 'rb')
    mail_text = read_report.read()
    read_report.close()

    use_email = 'zhenhongpan@maphive.io'
    email_password = 'Pancars123'
    sender = 'zhenhongpan@maphive.io'
    # receiver = ['zhenhongpan@maphive.io', 'junganwang@locision.com', 'ethanwang@mapxus.com']
    receiver = ['zhenhongpan@maphive.io']

    subject = u'Unit Test Report'
    msg = MIMEText(mail_text, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receiver)

    email_server = smtplib.SMTP_SSL('smtp.exmail.qq.com', '465')
    email_server.helo('smtp.exmail.qq.com')
    email_server.ehlo('smtp.exmail.qq.com')
    email_server.login(use_email, email_password)

    try:
        email_server.sendmail(sender, receiver, msg.as_string())
        email_server.quit()
    except Exception, error:
        logging.error(error)


def FindHtmlReport(reportPath):
    report_lists = os.listdir(reportPath)
    for reports in report_lists:
        if os.path.splitext(reports)[1] == '.html':
            # print reports
            fp = reportPath + '/' + reports
            print u'最新的测试报告是：' + fp
            return fp


def NewReportPath(report_dir):
    lists = os.listdir(report_dir)
    # print(lists)
    # 按时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '/' + fn))
    print(u"最新测试报告文件夹是:" + lists[-1])

    fp = os.path.join(report_dir, lists[-1])
    return fp
