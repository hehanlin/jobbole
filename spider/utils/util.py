# -*- coding: utf-8 -*-

import random
import re
import time
from spider import consts
from spider.consts import WORK_YEARS_STORE_DICT


def update_salary_dict(salary_dict, start, end):
    if len(salary_dict) == 0:
        salary_dict = {i: 0 for i in range(0, 111)}
    for index in range(start, end + 1):
        salary_dict[index] += 1
    return salary_dict


def get_salary_section(string):
    """
    e.g:
    15k-25k  ->  (15, 25)
    15k以上  ->  (15, 20)
    15k以下  ->  (10, 15)
    :param string: 15k-25k
    :return: 15,25
    """
    pattern = r'K|k|以上|以下'
    replace_char = ''

    if string.find('-') != -1:
        string = re.sub(pattern=pattern, repl=replace_char, string=string)
        start, end = string.split('-')
    elif string.endswith('以下'):
        string = re.sub(pattern=pattern, repl=replace_char, string=string)
        start, end = int(string) - 5 if int(string) - 5 >= 0 else 1, string
    elif string.endswith('以上'):
        string = re.sub(pattern=pattern, repl=replace_char, string=string)
        start, end = string, int(string) + 5
    else:
        raise Exception('error salary' + string)

    return int(start), int(end)


def get_work_years(string):
    for key,value in WORK_YEARS_STORE_DICT.items():
        if string == key:
            return value
    return WORK_YEARS_STORE_DICT['unknown']


def reverse_dict(old_dict):
    return {value: key for (key, value) in old_dict.items()}


def crawler_sleep():
    """爬虫休眠"""
    time.sleep(random.uniform(consts.MIN_SLEEP_TIME, consts.MAX_SLEEP_TIME))
