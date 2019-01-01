# coding=utf-8

from BaseActionMethod import BaseDriver
from BaseMethod.BaseCV import image
from BaseMethod import Error
import os
import time


class CvDriver(object):
    def __init__(self, _driver):
        self.driver = _driver
        self.base = BaseDriver(self.driver)

    def click_image(self, original, target, precision=0.9):
        """
        点击图片
        :param original:
        :param target:
        :param precision
        :return:
        """
        point = image(original, target, precision)
        if point:
            self.driver.tap([point])
            return True
        else:
            raise Error.NoFoundTargetImage('No found image! The original image does not contain the target image!')

    def input_text(self, original, target, value, precision=None):
        """
        android 专用
        :param original:
        :param target:
        :param value:
        :param precision:
        :return:
        """
        try:
            if self.click_image(original, target, precision):
                os.system('adb shell input text' + str(value))
        except Exception as e:
            raise Exception(e)

    @staticmethod
    def wait_image(original, target, precision=None, wait_time=10):
        start_time = time.time()
        point = image(original, target, precision)
        if point:
            wait_time = 3
            time.sleep(wait_time)
            return True
        elif point is False:
            diff = time.time() - start_time
            if diff < wait_time:
                print 'sleep time is' + str(diff)
                time.sleep(diff)
            else:
                time.sleep(wait_time)
