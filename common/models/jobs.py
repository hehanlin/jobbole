# -*- coding: utf-8 -*-

from common.instances import BaseModel
from playhouse.postgres_ext import ArrayField, JSONField, PrimaryKeyField, CharField, IntegerField


class Jobs(BaseModel):
    id = PrimaryKeyField()
    title = CharField(help_text=u'职位标题')
    work_years = ArrayField(help_text=u'工作年限')
    city_id = IntegerField(help_text=u'城市 id')
    #TODO:公司信息
    salarys = ArrayField(help_text=u'薪水范围')
    eduction = CharField(help_text=u'教育背景')
    from_site = IntegerField(help_text=u'来自网站 1 boss 2 lagou 3 智联')
    detail = JSONField(help_text=u'具体描述')


