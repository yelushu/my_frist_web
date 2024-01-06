# -*- coding: utf-8 -*-
DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:yelushu7758258@localhost/food_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8mb4"
SERVER_PORT = 8999



AUTH_COOKIE_NAME = "mooc_food"#配置的cook
JSON_AS_ASCII=False#防止页面乱码

#过滤url
IGNORE_URLS = [
    "^/user/login"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

API_IGNORE_URLS = [
    "^/api"
]

PAGE_SIZE=50#分页行数
PAGE_DISPLAY=10#分页数

STATUS_MAPPING={
    '1':'正常',
    '0':'已删除'

}
#小程序相关信息
MINA_APP={
    'app_id':'wxb91a2c31bb9caac2',
    'app_key':'8fa753c8e7c9d76b428280b4592d0f2c',
    'paykey':'xxxxxxxxxxxxxx换自己的',
    'mch_id':'xxxxxxxxxxxx换自己的',
    'callback_url':'/api/order/callback'

}

APP = {
    'domain':'http://127.0.0.1:8999/api/'
}


UPLOAD = {
    'ext':[ 'jpg','gif','bmp','jpeg','png' ],
    'prefix_path':'/web/controllers/upload/20231223/',
    'prefix_url':'/web/controllers/upload/20231223/'#todo：需要到UrlManager的buildImageUrl中，修改读取图片的路径
}

PAY_STATUS_MAPPING = {
    "1":"已支付",
    "-8":"待支付",
    "0":"已关闭"
}

PAY_STATUS_DISPLAY_MAPPING = {
    "0":"订单关闭",
    "1":"支付成功",
    "-8":"待支付",
    "-7":"待发货",
    "-6":"待确认",
    "-5":"待评价"
}