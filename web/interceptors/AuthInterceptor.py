# -*- coding: utf-8 -*-
#用于web端：用户身份识别和查询该用户是否存在
from application import app
from flask import request,g,redirect

from common.models.User import  User
from common.libs.user.UserService import UserService
from common.libs.UrlManager import  UrlManager
from common.libs.LogService import LogService
import  re
@app.before_request
def before_request():
    ignore_urls = app.config['IGNORE_URLS']
    ignore_check_login_urls = app.config['IGNORE_CHECK_LOGIN_URLS']
    path = request.path


    # 如果是静态文件就不要查询用户信息了
    pattern = re.compile('%s' % "|".join(ignore_check_login_urls))
    if pattern.match(path):
        return

    if '/api' in path:
        return


    user_info = check_login()
    g.current_user = None #获取当前用户信息，用于传到html模版里，实时更新显示信息
    if user_info:
        g.current_user = user_info

#    加入日志
    LogService.addAccessLog()
    pattern = re.compile('%s' % "|".join(ignore_urls))
    if pattern.match(path):
        return

    if not user_info :
        return redirect( UrlManager.buildUrl( "/user/login" ) )
    #
    return


# '''

# '''
def check_login():
    cookies = request.cookies
    auth_cookie = cookies[app.config['AUTH_COOKIE_NAME']] if app.config['AUTH_COOKIE_NAME'] in cookies else None


    if '/api' in request.path:
        app.logger.info(request.path)
        auth_cookie = request.headers.get("Authorization")
        app.logger.info( request.headers.get("Authorization") )

    if auth_cookie is None:
        return False

    auth_info = auth_cookie.split("#")#授权码由#组成，切分后就可以识别身份
    if len(auth_info) != 2:
        return False

    try:
        user_info = User.query.filter_by(uid=auth_info[1]).first()#查到到数据，说明人是存在的
    except Exception:
        return False

    if user_info is None:
        return False

    if auth_info[0] != UserService.geneAuthCode( user_info ):
        return False

    if user_info.status != 1:
        return False

    return user_info