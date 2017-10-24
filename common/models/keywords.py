# -*- coding: utf-8 -*-

from peewee import PrimaryKeyField, CharField
from common.instances import BaseModel


class Keywords(BaseModel):
    """
    搜索关键字
    """
    id = PrimaryKeyField()
    keyword = CharField()