# coding=utf-8

import AppiumDriverDocker
import AppiumDriverLocal

"""'http://172.17.3.48:4723/wd/hub'"""
# link=None
# link='http://172.17.3.48:4723/wd/hub'


def LocalOrDocker(link=None):
    """（华为）判断是否有link，没有则属于本地"""
    if link is None:
        print u'appium 地址为localhost'
        return AppiumDriverLocal.__MappyBeeDriver__()
    else:
        print u'appium 地址为docker'
        return AppiumDriverDocker.__DockerDriver__(link)


def LocalOrDockerUiAuto(link=None):
    """(小米)判断是否有link，没有则属于本地,Ui auto 自动化测试引擎"""
    if link is None:
        print u'appium 地址为localhost'
        return AppiumDriverLocal.__MappyBeeDriverUiAuto()
    else:
        print u'appium 地址为docker'
        return AppiumDriverDocker.__DockerDriverUiAuto__(link)
