# -.- encoding: utf-8 -.-
#
# 後台管理
#

from bottle import route
from bottle import jinja2_view as view
from bottle import jinja2_template as template
from bottle import TEMPLATE_PATH
from db import cur

@route('/admin')
@route('/admin/')
@route('/admin/info')
@view('admin/info.html')
def admin_info():
    return {'name': 'admin_info()'}

@route('/admin/doc/detail')
@view('admin/doc_detail.html')
def admin_doc_detail():
    docId = '1030393A'
    cur.execute('SELECT * FROM docs WHERE id=?',(docId,))
    row = cur.fetchone()
    return row
