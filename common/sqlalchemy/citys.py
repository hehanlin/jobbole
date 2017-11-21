# -*- coding: utf-8 -*-

from common.sqlalchemy import BaseModel
from sqlalchemy import Column, INTEGER, VARCHAR, text


class Citys(BaseModel):
    __tablename__ = 'citys'

    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR, doc='城市名')
    boss_code = Column(VARCHAR, doc='boss直聘代码')
    lagou_code = Column(VARCHAR, doc='logou代码')
    zhilian_code = Column(VARCHAR, doc='智联代码')
    
    @classmethod
    def init_data(cls):
        sql = text("""
            INSERT INTO citys VALUES ('1', '全国', '100010000', '全国', '全国');
            INSERT INTO citys VALUES ('2', '北京', '101010100', '北京', '北京');
            INSERT INTO citys VALUES ('3', '上海', '101020100', '上海', '上海');
            INSERT INTO citys VALUES ('4', '广州', '101280100', '广州', '广州');
            INSERT INTO citys VALUES ('5', '深圳', '101280600', '深圳', '深圳');
            INSERT INTO citys VALUES ('6', '杭州', '101210100', '杭州', '杭州');
            INSERT INTO citys VALUES ('7', '天津', '101030100', '天津', '天津');
            INSERT INTO citys VALUES ('8', '西安', '101110100', '西安', '西安');
            INSERT INTO citys VALUES ('9', '苏州', '101190400', '苏州', '苏州');
            INSERT INTO citys VALUES ('10', '武汉', '101200100', '武汉', '武汉');
            INSERT INTO citys VALUES ('11', '厦门', '101230200', '厦门', '厦门');
            INSERT INTO citys VALUES ('12', '长沙', '101250100', '长沙', '长沙');
            INSERT INTO citys VALUES ('13', '成都', '101270100', '成都', '成都');
            INSERT INTO citys VALUES ('14', '重庆', '101040100', '重庆', '重庆');
            INSERT INTO citys VALUES ('16', '南京', '101190100', '南京', '南京');
            INSERT INTO citys VALUES ('17', '郑州', '101180100', '郑州', '郑州');
            INSERT INTO citys VALUES ('18', '太原', '101100100', '太原', '太原');
        """)
        cls.session.execute(sql)
        cls.session.commit()

    @classmethod
    def list(cls):
        query = cls.session.query(cls)
        return query.all()