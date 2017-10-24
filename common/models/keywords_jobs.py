# -*- coding: utf-8 -*-

from peewee import IntegerField
from common.instances import BaseModel


class Keywords_Jobs(BaseModel):
    """
    关键字与工作关联表
    """
    keywords_id = IntegerField()
    jobs_id = IntegerField()