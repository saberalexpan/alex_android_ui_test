# coding=utf-8

import unittest
from MappyBee.Case.TestCases01Register import RegisterTestCases
from MappyBee.Case.TestCases02Login import LoginTestCases
from MappyBee.Case.TestCases03Search import SearchTestCases
from MappyBee.Case.TestCases04Sample import SampleTestCases
from MappyBee.Case.TestCases05HistorySample import SampleHistoryTestCases
from MappyBee.Case.TestCases06Setting import SettingTestCases


def CreateTestCasesContainer_1():
    """
    小米
    创建1号测试容器
    :return:
    """
    tests_cases_container = unittest.TestSuite()
    suite_0 = unittest.makeSuite(RegisterTestCases)
    suite_1 = unittest.makeSuite(LoginTestCases)
    suite_2 = unittest.makeSuite(SearchTestCases)
    suite_3 = unittest.makeSuite(SettingTestCases)

    tests_cases_container.addTests([suite_0, suite_1, suite_2, suite_3])
    # tests_cases_container.addTest(suite_1)

    print tests_cases_container.countTestCases()
    print tests_cases_container
    return tests_cases_container


def CreateTestCasesContainer_2():
    """
    华为
    创建2号测试容器
    :return:
    """
    tests_cases_container = unittest.TestSuite()
    suite_0 = unittest.makeSuite(SampleTestCases)
    suite_1 = unittest.makeSuite(SampleHistoryTestCases)

    tests_cases_container.addTests([suite_0, suite_1])

    print tests_cases_container.countTestCases()
    print tests_cases_container
    return tests_cases_container


container_1 = CreateTestCasesContainer_1()
container_2 = CreateTestCasesContainer_2()
