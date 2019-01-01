# coding=utf-8

import cv2
import logging


"""
openCV2 match templates匹配模式：
    CV_TM_SQDIFF 平方差匹配法：该方法采用平方差来进行匹配；最好的匹配值为0；匹配越差，匹配值越大。

    CV_TM_CCORR 相关匹配法：该方法采用乘法操作；数值越大表明匹配程度越好。
                    
    CV_TM_CCOEFF 相关系数匹配法：1表示完美的匹配；-1表示最差的匹配。

    CV_TM_SQDIFF_NORMED 归一化平方差匹配法

    CV_TM_CCORR_NORMED 归一化相关匹配法

    CV_TM_CCOEFF_NORMED 归一化相关系数匹配法

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
"""


def image(original_image, target_image, precision=0.9, image_method=cv2.TM_CCOEFF_NORMED):
    """
    查找图片，验证模板图是否存在于匹配图上
    :param original_image:匹配图，原图
    :param target_image:
    :param precision:
    :param image_method:
    :return:
    """
    # 读取图片，并对图像进行灰度处理
    original = cv2.imread(original_image, 0)
    target = cv2.imread(target_image, 0)
    target_height, target_width = target.shape[::]

    # 图像识别，返回数值矩阵
    result = cv2.matchTemplate(original, target, image_method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    logging.info(min_val, max_val, min_loc, max_loc)

    if max_val <= precision:
        logging.error('no found target image!')
        print '(max:' + str(max_val), 'expect:' + str(precision) + ')'
        return False
    else:
        print max_val

    # 计算各个点坐标
    point_up_left = max_loc

    point_low_right = (max_loc[0] + target_width, max_loc[1] + target_height)

    point_center = (max_loc[0] + (target_width / 2), max_loc[1] + (target_height / 2))

    print u'左上角坐标为：' + str(point_up_left)

    print u'右下角坐标为：' + str(point_low_right)

    print u'中心点坐标为：' + str(point_center)

    return point_center


def image_low_right_point(original_image, target_image, precision=0.9, image_method=cv2.TM_CCOEFF_NORMED):
    """
    查找图片，验证模板图是否存在于匹配图上
    :param original_image:匹配图，原图
    :param target_image:
    :param precision:
    :param image_method:
    :return:
    """
    # 读取图片，并对图像进行灰度处理
    original = cv2.imread(original_image, 0)
    target = cv2.imread(target_image, 0)
    target_height, target_width = target.shape[::]

    # 图像识别，返回数值矩阵
    result = cv2.matchTemplate(original, target, image_method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    logging.info(min_val, max_val, min_loc, max_loc)

    if max_val <= precision:
        logging.error('no found target image!')
        print '(max:' + str(max_val), 'expect:' + str(precision) + ')'
        return False
    else:
        print max_val

    # 计算各个点坐标
    point_up_left = max_loc

    point_low_right = (max_loc[0] + target_width, max_loc[1] + target_height)

    point_center = (max_loc[0] + (target_width / 2), max_loc[1] + (target_height / 2))

    print u'左上角坐标为：' + str(point_up_left)

    print u'右下角坐标为：' + str(point_low_right)

    print u'中心点坐标为：' + str(point_center)

    return point_low_right
