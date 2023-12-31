# coding: utf-8
from application import db#使用统一的db



class FoodCat(db.Model):
    __tablename__ = 'food_cat'


    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='类别名称')
    weight = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='权重')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态 1：有效 0：无效')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最后一次更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='插入时间')
