# -.- encoding: utf-8 -.-
#
# RESTful API
#

import json

from time import ctime

from bottle import hook
from bottle import route
from bottle import request
from bottle import response

from db import cur

API_VERSION = 0.1

@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'

@route('/api', methohd='GET')
@route('/api/status', method='GET')
def api_status():
    return {'api_version':API_VERSION, 'server_status':'online', 'server_time': ctime()}

@route('/api/summary',method='GET')
def api_summary():
    watch = request.query.watch
    responseData = _fake_summary_json(watch)

    return json.dumps(responseData)

@route('/api/test', method='GET')
def api_test():

    return json.dumps(_summary_dev_pass())

def _summary_dev_pass():
    sql_script = """
        SELECT devunit, count(*) count FROM details
        WHERE devunit != ""
        GROUP BY devunit ORDER BY count DESC
        LIMIT 10
    """
    cur.execute(sql_script)
    row = cur.fetchall()

    return row

def _fake_summary_json(watch):
    fake_data = {
        'city_area': [
        {
            "city" : "台北市",
            "area" : 100,
            "unit" :  "公頃"
        },
        {
            "city" : "新北市",
            "area" : 80,
            "unit" :  "公頃"
        }
        ],
        'dev_pass' :
        {
            "dev" : "遠雄",
            "count" : 20
        }
    }

    if fake_data.has_key(watch):
        return fake_data[watch]

    return {}

