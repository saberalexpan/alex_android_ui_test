# coding=utf-8

from selenium import webdriver
import logging


def start_driver(name, local_storage=None, log_file=None):
    """
    web driver 启动浏览器使用，支持使用local storage
    :param name: 浏览器名称
    :param local_storage: local storage保存路径（或者Chrome默认存在local storage的路径）
    :param log_file:浏览器运行日志保存路径（需要建立一个后缀名.log的文件）【此处可以为空，非必填】
    :return:
    """
    try:
        if name == u'chrome' or name == u'Chrome':
            logging.info(u'browser was opened')
            if local_storage is not None and local_storage is not None:
                setting = webdriver.ChromeOptions()
                setting.add_argument(local_storage)
                driver = webdriver.Chrome(chrome_options=setting, service_log_path=log_file)
                return driver
            elif local_storage is None and local_storage is None:
                driver = webdriver.Chrome()
                return driver
        elif name == u'ie' or name == u'Ie' or u'IE':
            logging.info(u'browser was opened')
            driver = webdriver.Ie()
            return driver
        elif name == u'firefox' or name == u'FireFox' or name == u'ff':
            logging.info(u'browser was opened')
            driver = webdriver.Firefox()
            return driver
        elif name == u'safari' or name == u'Safari':
            logging.info(u'browser was opened')
            driver = webdriver.Safari()
            return driver
        else:
            logging.error(u'no found this browser,please try another values,such as(chrome,ie,firefox,safari)')
    except Exception:
        raise Exception('浏览器出现异常: %s')
