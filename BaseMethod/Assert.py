# coding=utf-8

from BaseActionMethod.BaseActionMethod import BaseDriver
from BaseMethod import Error
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import exceptions as ex
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class Assert(BaseDriver):
    def element_text_assert(self, attribute, loc, text=None):
        if text is None:
            try:
                WebDriverWait(self.driver, 10).until(
                    lambda driver:
                    self.driver.find_element(self.__attribute__(attribute), loc).is_displayed()
                )
                assert_text = self.get_text(attribute, loc)
                element_text = self.get_text(attribute, loc)
                self.value_equal(assert_text, element_text, msg='Assert Fail %s' % element_text)
            except Exception as msg:
                raise Exception(msg)
            except ex.TimeoutException:
                raise Exception(u'time out')
        elif text is not None:
            try:
                WebDriverWait(self.driver, 10).until(
                    lambda driver:
                    self.driver.find_element(self.__attribute__(attribute), loc).is_displayed()
                )
                assert_text = text
                element_text = self.get_text(attribute, loc)
                self.value_equal(assert_text, element_text, msg='Assert Fail %s' % element_text)
            except Exception as msg:
                raise Exception(msg)
            except ex.TimeoutException:
                raise Exception(u'time out')

    def element_is_in_this_page(self, attribute, loc, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((self.__attribute__(attribute), loc)))
            print u'%s is in the Page!' % loc
            return True
        except ex.NoSuchElementException:
            raise Error.NoFoundElement('No found element! %s' % loc)
        except ex.TimeoutException:
            raise Error.TimeOutError('Time out! %s' % timeout)

    def element_is_not_in_this_page(self, attribute, loc, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until_not(ec.visibility_of_element_located((self.__attribute__(attribute), loc)))
            print u'%s not in the page!' % loc
            return True
        except ex.NoSuchElementException:
            raise Error.NoFoundElement('No found element! %s' % loc)
        except ex.TimeoutException:
            raise Error.TimeOutError('Time out! %s' % timeout)

    @staticmethod
    def value_equal(first_value, second_value, msg=''):
        """
        断言值相等
        :param first_value:
        :param second_value:
        :param msg:
        :return:
        """
        if first_value != second_value:
            raise Error.AssertFailError(msg)
        else:
            print u'Assert Pass! %s %s' % (str(first_value), str(second_value))
            return True

    @staticmethod
    def value_not_equal(first_value, second_value, msg):
        """
        断言值不相等
        :param first_value:
        :param second_value:
        :param msg:
        :return:
        """
        if first_value == second_value:
            raise Error.AssertFailError(msg)
        else:
            print u'Assert Pass! %s %s' % (str(first_value), str(second_value))
            return True

    @staticmethod
    def __attribute__(value):
        if value == 'id':
            el_type = By.ID
            return el_type
        elif value == 'xpath':
            el_type = By.XPATH
            return el_type
        elif value == 'android':
            el_type = MobileBy.ANDROID_UIAUTOMATOR
            return el_type
        elif value == 'android_accessibility_id' or 'android_id':
            el_type = MobileBy.ACCESSIBILITY_ID
            return el_type
