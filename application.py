# -*- coding: utf-8 -*-
from flask import Flask

from flask_script import Manager

from flask_sqlalchemy import SQLAlchemy
import pymysql #因为flask自带的sql很烂，所以需要导入pymysql进行补充，在配置文档里，地址也需要加上pymysql
import os
class Application( Flask ):
    def __init__(self,import_name):

        super( Application,self ).__init__( import_name)
        self.config.from_pyfile( 'config/local_setting.py' )

        if "ops_config" in os.environ:
            self.config.from_pyfile( 'config/%s_setting.py'%os.environ['ops_config'] )

        db.init_app( self )

db = SQLAlchemy()

app = Application( __name__)

manager = Manager( app )
from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildStaticUrl,'buildStaticUrl')#因为url和版本进行管理了（在UrlManager中），需要通过这个函数把管理函数传到html中
app.add_template_global(UrlManager.buildUrl,'buildUrl')
app.add_template_global(UrlManager.buildImageUrl, 'buildImageUrl')




#
#
# # -*- coding: utf-8 -*-
# from flask import Flask
#
# from flask_script import Manager
#
# from flask_sqlalchemy import SQLAlchemy
# import pymysql #因为flask自带的sql很烂，所以需要导入pymysql进行补充，在配置文档里，地址也需要加上pymysql
# import os
# class Application( Flask ):
#     def __init__(self,import_name,template_folder=None,root_path=None):
#         print(os.getcwd() + '/web/template/')
#         super( Application,self ).__init__( import_name,template_folder=template_folder,root_path=root_path ,static_folder=None)
#         self.config.from_pyfile( 'config/local_setting.py' )
#
#         if "ops_config" in os.environ:
#             self.config.from_pyfile( 'config/%s_setting.py'%os.environ['ops_config'] )
#
#         db.init_app( self )
#
# db = SQLAlchemy()
#
# app = Application( __name__ ,template_folder=os.getcwd()+"/web/templates/",root_path=os.getcwd())
#
# manager = Manager( app )
# from common.libs.UrlManager import UrlManager
# app.add_template_global(UrlManager.buildStaticUrl,'buildStaticUrl')#因为url和版本进行管理了（在UrlManager中），需要通过这个函数把管理函数传到html中
# app.add_template_global(UrlManager.buildUrl,'buildUrl')
#

