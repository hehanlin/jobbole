# -*- coding: utf-8 -*-

from peewee import PrimaryKeyField, IntegerField, CharField
from common.instances import BaseModel


class Citys(BaseModel):
    """
    城市列表
    """
    id = PrimaryKeyField()
    name = CharField(help_text=u'城市名')
    boss_code = IntegerField(help_text=u'boss直聘代码')
    lagou_code = IntegerField(help_text=u'logou代码')
    zhilian_code = IntegerField(help_text=u'智联代码')