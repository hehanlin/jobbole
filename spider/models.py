# -*- coding: utf-8 -*-

from mongoengine import Document, StringField
import common.instances


class JobTags(Document):
    tag = StringField()

