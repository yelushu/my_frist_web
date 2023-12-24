# -*- coding: utf-8 -*-
import time
from application import  app
class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl( path ):
        return path

    @staticmethod
    def buildStaticUrl(path):
        release_version = app.config.get( 'RELEASE_VERSION' )
        ver = "%s"%( int( time.time() ) ) if not release_version else release_version
        path =  "/static" + path + "?ver=" + ver
        return UrlManager.buildUrl( path )

    @staticmethod

    def buildImageUrl( path ):#传入文件名
        app_config = app.config['APP']
        #url = app_config['domain'] + app.config['UPLOAD']['prefix_url'] + path
        url=app.root_path + app.config['UPLOAD']['prefix_url']+ path
        #url = app.root_path + + app.config['UPLOAD']['prefix_url'] + path#上面是对的，但是路径错误，需要修改。
        print('urlss'+url)
        return url