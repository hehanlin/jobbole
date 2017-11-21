# -*- coding: utf-8 -*-

from common.sqlalchemy import BaseModel
from sqlalchemy import Column, INTEGER


class KeywordsJobs(BaseModel):
    __tablename__ = 'keywords_jobs'

    id = Column(INTEGER, primary_key=True)
    keywords_id = Column(INTEGER)
    jobs_id = Column(INTEGER)
