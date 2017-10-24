# -*- coding: utf-8 -*-


def create_tables():
    from common.instances import db
    from common.models.keywords import Keywords
    from common.models.citys import Citys
    from common.models.keywords_jobs import Keywords_Jobs
    from common.models.jobs import Jobs
    try:
        db.create_tables([
            Keywords,
            Citys,
            Keywords_Jobs,
            Jobs
        ])
    except:
        pass

