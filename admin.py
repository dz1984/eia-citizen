# -.- encoding: utf-8 -.-
#
# 後台管理
#

from bottle import route
from bottle import jinja2_view as view
from bottle import jinja2_template as template
from bottle import TEMPLATE_PATH

@route('/admin')
@route('/admin/')
@route('/admin/info')
@view('admin/info.html')
def admin_info():
	return {'name': 'admin_info()'}
