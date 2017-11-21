# -*- coding: utf-8 -*-

from common.sqlalchemy import BaseModel
from sqlalchemy import Column, VARCHAR, INTEGER, TEXT, text
from sqlalchemy.exc import InvalidRequestError


class Jobs(BaseModel):
    __tablename__ = 'jobs'

    id = Column(INTEGER, primary_key=True)
    url = Column(VARCHAR, doc='职位链接', unique=True)
    title = Column(VARCHAR, doc='职位标题')
    work_years = Column(VARCHAR, doc='工作年限')
    city = Column(VARCHAR, doc='城市')
    # TODO:公司信息
    salarys = Column(VARCHAR, doc='薪水范围')
    eduction = Column(VARCHAR, doc='教育背景')
    from_site = Column(INTEGER, doc='来自网站 1 boss 2 lagou 3 智联')
    detail = Column(TEXT, doc='具体描述')

    @classmethod
    def upsert(cls, data):
        try:
            sql = text("""
                WITH upsert_jobs AS (
                    INSERT INTO jobs (
                        url, title, work_years, city, salarys, eduction, from_site, detail
                    )
                    VALUES(
                            :url,
                            :title,
                            :work_years,
                            :city,
                            :salarys,
                            :eduction,
                            :from_site,
                            :detail
                        ) 
                    ON conflict (url) DO UPDATE
                        SET url = EXCLUDED.url,
                            title = EXCLUDED.title,
                            work_years = EXCLUDED.work_years,
                            city = EXCLUDED.city,
                            salarys = EXCLUDED.salarys,
                            eduction = EXCLUDED.eduction,
                            from_site = EXCLUDED.from_site,
                            detail = EXCLUDED.detail
                    RETURNING *
                ),
                upsert_keywords_jobs AS (
                    INSERT INTO keywords_jobs (
                        keywords_id,
                        jobs_id
                    )
                    SELECT :keywords_id, upsert_jobs.id FROM upsert_jobs
                        WHERE NOT EXISTS(
                            SELECT * FROM keywords_jobs WHERE keywords_id = :keywords_id AND jobs_id = upsert_jobs.id
                        )
                    RETURNING *
                )
                SELECT id FROM upsert_jobs
            """)
            query = cls.session.execute(sql, data)
            cls.session.commit()
            res = query.fetchone()
            sql = text("SELECT * FROM keywords_jobs WHERE keywords_id = :keywords_id AND jobs_id = :jobs_id")
            query = cls.session.execute(sql, {'keywords_id': data['keywords_id'],
                                              'jobs_id': res[0]})
            cls.session.commit()
            res = query.fetchone()
            return res
        except InvalidRequestError as e:
            cls.session.rollback()
            raise e
