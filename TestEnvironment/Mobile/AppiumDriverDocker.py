# coding=utf-8

"""
app ium docker 启动配置
"""

from appium import webdriver


def __DockerDriver__(myDocker):
    """本地配置的docker driver
        :param myDocker ：本地docker部署的AppIum的连接地址
        Use : driver = __DockerDriver__('http://172.17.3.136:4723/wd/hub')
    """
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
        # 指定本地或者docker容器apk存放的路径
        # 'app': mb_path
    }
    driver = webdriver.Remote(myDocker, cap)
    return driver


def __DockerDriverUiAuto__(myDocker):
    """本地配置的docker driver
        UI auto 自动化引擎
        :param myDocker ：本地docker部署的AppIum的连接地址
        Use : driver = __DockerDriver__('http://172.17.3.136:4723/wd/hub')
    """
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
        # 指定本地或者docker容器apk存放的路径
        # 'app': mb_path
    }
    driver = webdriver.Remote(myDocker, cap)
    return driver
