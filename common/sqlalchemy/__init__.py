# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from common.settings import Config
DB_engine = create_engine(Config.DATABASE_URL)
_BaseModel = declarative_base()
_Session = sessionmaker(bind=DB_engine)


class BaseModel(_BaseModel):
    __abstract__ = True
    __metadata__ = MetaData(bind=DB_engine)
    session = _Session(autocommit=False)

    @classmethod
    def add_many(cls, items: list):
        global DB_engine
        return DB_engine.execute(
            cls.__table__.insert(),
            items
        )


def create_tables():
    from common.sqlalchemy.citys import Citys
    from common.sqlalchemy.jobs import Jobs
    from common.sqlalchemy.keywords import Keywords
    from common.sqlalchemy.keywords_jobs import KeywordsJobs
    from spider.keywords import update_keywords_data
    BaseModel.metadata.drop_all(DB_engine)
    BaseModel.metadata.create_all(DB_engine)
    Citys.init_data()
    update_keywords_data()