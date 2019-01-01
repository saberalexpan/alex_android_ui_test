# coding=utf-8

import os
import re
import axmlparserpy.apk as apk
import logging


'''
动态分析APK包的信息，确保Appium启动参数的时效性
'''


def read_app(apk_path):
    read_app_path = apk_path
    app = apk.APK(read_app_path)
    return app


def get_apk_package_name(apk_path):
    get_app_package_name = read_app(apk_path).get_package()
    return get_app_package_name


def get_app_activity(apk_path, target_activity):
    app_activity = target_activity
    all_app_activity = read_app(apk_path).get_activities()
    if app_activity in all_app_activity:
        logging.info('surefire activity')
        return app_activity
    else:
        logging.error(all_app_activity)
        raise Exception('activity is no existed')


def get_devices_id():
    readDeviceId = list(os.popen('adb devices').readlines())
    deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
    # print deviceId
    return deviceId


def get_android_version():
    os_version = os.popen('adb shell getprop ro.build.version.release').read()
    # print os_version
    return os_version
