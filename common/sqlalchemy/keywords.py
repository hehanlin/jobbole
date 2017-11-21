# -*- coding: utf-8 -*-

from common.sqlalchemy import BaseModel
from sqlalchemy import Column, INTEGER, VARCHAR


class Keywords(BaseModel):
    __tablename__ = 'keywords'

    id = Column(INTEGER, primary_key=True)
    keyword = Column(VARCHAR)

    @classmethod
    def list(cls, keyword=None):
        query = cls.session.query(cls)
        if keyword:
            query = query.filter(cls.keyword.like('%' + keyword + '%'))
        return query.all()
