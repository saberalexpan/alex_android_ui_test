# coding=utf-8

"""
appium 启动参数配置
"""

# from TestEnvironment.Mobile import Devices
from appium import webdriver
# import os

# myAppPath = '/Users/alex.pan/Documents/Android_Ui/MappyBee_2.5.0-alpha.1_integration.apk'


def __MappyBeeDriver__():
    """本地使用"""
    cap = {
        'platformName': 'Android',
        'platformVersion': '8.0.0',
        'deviceName': 'RTJ0217726002388',
        'appPackage': 'io.maphive.mappybee',
        'appActivity': 'io.maphive.mappybee.activity.WelcomeActivity',
        'noReset': True,
        # 解决appIum中文输入问题
        'resetKeyboard': True,
        'unicodeKeyboard': True,
        'automationName': "UiAutomator2"
        # 'app': myAppPath
    }
    driver = webdriver.Remote('http://localhost:4724/wd/hub', cap)
    return driver


def __MappyBeeDriverUiAuto():
    """本地使用
        UI auto 自动化引擎"""
    cap = {
        'platformName': 'Android',
        'platformVersion': '6.0.1',
        'deviceName': 'fb77ec48',
        'appPackage': 'io.maphive.mappybee',
        'appActivity': 'io.maphive.mappybee.activity.WelcomeActivity',
        'noReset': True,
        # 解决appIum中文输入问题
        'resetKeyboard': True,
        'unicodeKeyboard': True,
        # 'automationName': "UiAutomator2"
        # 'app': myAppPath
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', cap)
    return driver
