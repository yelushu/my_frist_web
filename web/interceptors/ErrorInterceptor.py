# -*- coding: utf-8 -*-
#如果运行期间报错，引导到这个页面
from application import  app
from common.libs.Helper import ops_render
from common.libs.LogService import LogService

@app.errorhandler( 404 )
def error_404( e ):
    LogService.addErrorLog( str( e ) )
    return ops_render( 'error/error.html',{ 'status':404,'msg':'很抱歉！您访问的页面不存在' } )