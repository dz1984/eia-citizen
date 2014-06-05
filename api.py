# -.- encoding: utf-8 -.-
#
# RESTful API
#

import time

from bottle import route
from bottle import jinja2_view as view
from bottle import jinja2_template as template
from bottle import TEMPLATE_PATH
from db import cur

API_VERSION = 0.1

@route('/api')
@route('/api/status')
def api_status():
    return {'api_version':API_VERSION, 'server_status':'online', 'server_time':time.time()}
