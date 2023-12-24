# -*- coding: utf-8
# 用于网页注册，方便统一管理：每新增一个网页，需要在这里进行注册才能上线-*-
from application import app



"""
蓝图注册"""
from web.controllers.Index.index import route_index
from web.controllers.User.User import route_user
from web.controllers.Account.Account import route_account
from web.controllers.finance.Finance import route_finance
from web.controllers.Member.Member import route_member
from web.controllers.Food.food import route_food
from web.controllers.Stat.Stat import route_stat


"""
统一拦截处理和统一错误处理
"""

from web.interceptors.AuthInterceptor import  *
from web.interceptors.ApiAuthInterceptor import  *
from web.interceptors.ErrorInterceptor import  *

"API"
from web.controllers.api import route_api


from web.controllers.upload.Upload import route_upload
from web.controllers.chart import route_chart



#路由文件夹管理，url_prefix是统一的名称，在他的类中修改子路由
app.register_blueprint( route_index,url_prefix = "/" )
app.register_blueprint( route_user,url_prefix = "/user" )
app.register_blueprint( route_account,url_prefix = "/account" )
app.register_blueprint( route_finance,url_prefix = "/finance" )
app.register_blueprint( route_member,url_prefix = "/member" )
app.register_blueprint( route_food,url_prefix = "/food" )
app.register_blueprint( route_stat,url_prefix = "/stat" )
app.register_blueprint( route_api,url_prefix = "/api" )

app.register_blueprint( route_upload,url_prefix = "/upload" )
app.register_blueprint( route_chart,url_prefix = "/chart" )