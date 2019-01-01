# coding=utf-8

from BaseMethod import Error
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import exceptions as ex
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
import time
import os


class BaseDriver(object):
    def __init__(self, _driver):
        self.driver = _driver
        self.e = Error

    def find_element(self, attribute, loc):
        try:
            if attribute == 'id':
                el = self.driver.find_element(By.ID, loc)
                return el
            elif attribute == 'xpath':
                el = self.driver.find_element(By.XPATH, loc)
                return el
            elif attribute == 'android':
                el = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, loc)
                return el
            elif attribute == 'android_accessibility_id' or 'android_id':
                el = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, loc)
                return el
            else:
                raise self.e.ElementInputError('Element attributes is not exist!')
        except ex.NoSuchElementException:
            raise self.e.NoFoundElement('no found element')
        except Exception:
            raise Exception('NoFoundElement')

    def click_element(self, attribute, loc, first_click=True):
        try:
            if first_click:
                return self.find_element(attribute, loc).click()
        except ex.NoSuchElementException:
            raise self.e.NoFoundElement
        except Exception:
            raise Exception('NoFoundElement')

    def input_text(self, attribute, loc, value, first_click=True, first_clear=True):
        try:
            if first_click:
                self.click_element(attribute, loc)
            if first_clear:
                self.find_element(attribute, loc).clear()
            return self.find_element(attribute, loc).send_keys(value)
        except ex.NoSuchElementException:
            raise self.e.NoFoundElement
        except Exception:
            raise Exception('NoFoundElement')

    def get_element_size(self, attribute, loc):
        element = self.find_element(attribute, loc)
        coordinate_x = element.size['width']
        coordinate_y = element.size['height']
        # print coordinate_x, coordinate_y
        return coordinate_x, coordinate_y

    def get_windows_size(self, method=None):
        if method is None:
            window_size = self.driver.get_window_size()
            return window_size
        elif method is not None:
            window_size = self.driver.get_window_size()[method]
            return window_size

    # selenium 专用
    def keyboard(self, attribute, loc, key):
        """
        通过selenium---Key模块向网页发送特殊按键
        :param attribute: 元素属性
        :param loc: 元素位置
        :param key: 参数来源于Key模块（from selenium.webdriver.common.keys import Keys）
        :return:
        """
        try:
            target_el = self.find_element(attribute, loc)
            target_el.send_keys(key)
        except TypeError:
            raise TypeError(u'No found element')

    # appium 专用
    def key_code(self, value):
        """
        点击安卓手机上的实体健
        键盘按键值：
        https://testerhome.com/topics/1386
        :param value: 输入值为数字
        EX:
        self.key_code(29),发送键盘字母a
        :return:
        """
        return self.driver.keyevent(value)

    def get_text(self, attributes, loc):
        return self.find_element(attributes, loc).text

    def wait_element(self, attribute, loc):
        start_time = time.time()
        if self.__findElement__(attribute, loc) is False:
            sleep_time = time.time() - start_time
            print 'sleep time is: ' + str(sleep_time)
            time.sleep(sleep_time)
        elif self.__findElement__(attribute, loc):
            return True

    def __CustomPicturePath__(self, name, path=None):
        """创建图片路径"""
        if path is None:
            local_path = os.getcwd()
            path = local_path + '/' + name + '.png'
            return path
        elif path is not None:
            data = self.__data__()
            local_time = self.__localTime__()
            pic_format = '.png'
            path = path + '/' + data
            if os.path.exists(path):
                pic_path = path + '/' + name + '_' + local_time + pic_format
                return pic_path
            else:
                os.makedirs(path)
                pic_path = path + '/' + name + '_' + local_time + pic_format
                return pic_path

    def __findElement__(self, attributes, loc):
        try:
            WebDriverWait(self.driver, 10).\
                until(
                lambda driver: self.driver.find_element(attributes, loc).is_displayed()
            )
            return True
        except ex.NoSuchElementException:
            return False
        except ex.TimeoutException:
            return False

    @staticmethod
    def __data__():
        data = time.strftime('%Y_%m_%d', time.localtime(time.time()))
        return data

    @staticmethod
    def __localTime__():
        local_time = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
        return local_time

    @staticmethod
    def __ReturnWordFile__():
        path = os.getcwd()
        return path


class GetPicture(BaseDriver):
    """适用于安卓，web，iOS的截图方法
        方法中的路径：仅能用绝对路径（适用于本地调试）
    """
    def get_original_image(self, name, path=None):
        """获取素材原图（OpenCV方法用到）"""
        image_path = self.__CustomPicturePath__(name, path)
        self.__SavePicture__(name, path)
        return image_path

    def __SavePicture__(self, name, path=None):
        """保存图片，截图"""
        image = self.driver.get_screenshot_as_file(self.__CustomPicturePath__(name, path))
        return image


class GetPictureAndroid(BaseDriver):
    """这是用于安卓端的截图方法"""
    def get_original_picture(self, name):
        """适用adb的方法进行截图"""
        PicPath = os.getcwd() + '/OriginalImage/MappyBee'
        localTime = self.__localTime__()
        PicName = name + localTime + '.png'
        os.system('adb shell screencap -p /sdcard/' + PicName)
        time.sleep(2)
        os.system('adb pull /sdcard/' + PicName + ' ' + PicPath)
        Picture = PicPath + '/' + PicName
        print Picture
        return Picture
