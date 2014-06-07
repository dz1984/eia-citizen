# -.- encoding: utf-8 -.-
#
# RESTful API
#

from time import ctime

from bottle import route

API_VERSION = 0.1

@route('/api')
@route('/api/status')
def api_status():
    return {'api_version':API_VERSION, 'server_status':'online', 'server_time': ctime()}
