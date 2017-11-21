# -*- coding: utf-8 -*-

import requests
from common.instances import logging_instance
from lxml.etree import HTML
from spider.boss import http_headers
from common.sqlalchemy.jobs import Jobs as JobsModel

logger = logging_instance(__name__)


def update_job_detail_data(keyword_id: int, url: str)->None:
    data = request_job_detail(url)
    data['keywords_id'] = keyword_id
    res = JobsModel.upsert(data)
    print(res)


def request_job_detail(url: str)->dict:
    """
    请求job详情页，放入优先队列中
    :param url:
    :return:
    """
    try:
        resp = requests.get(url, headers=http_headers())
        data = parse_data(resp.text, url)
        logger.info("finish a job{}".format(data))
        return data
    except Exception as e:
        logger.error(e)


def parse_data(html: str, url: str)->dict:
    """
    解析数据
    :param html: str
    :param url: str
    :return: data: dict
    """
    try:
        html = HTML(html)
        job_primary_ele = html.xpath("//div[@class='job-primary']//div[@class='name']")[0]
        job_more_ele = html.xpath("//div[@class='job-primary']/div[@class='info-primary']/p[1]/text()")
        title = job_primary_ele.xpath("text()")[0]
        word_years = job_more_ele[1]
        city = job_more_ele[0]
        eduction = job_more_ele[2]
        salarys = job_primary_ele.xpath("span[@class='badge']/text()")[0]
        from_site = 1
        detail = html.xpath("//div[@class='job-detail']//div[@class='job-sec'][1]//text()")
        detail = ''.join([each.strip() for each in detail])
        return dict(
            url=url,
            title=title,
            work_years=word_years,
            city=city,
            eduction=eduction,
            salarys=salarys,
            from_site=from_site,
            detail=detail
        )
    except Exception as e:
        logger.error(e)

if __name__ == '__main__':
    update_job_detail_data(2, "http://www.zhipin.com/job_detail/1415141026.html")
