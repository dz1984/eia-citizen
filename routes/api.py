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

@route('/api/summary/:watch',method='GET')
def api_summary(watch):
    responseData = gen_summary_json(watch)

    return json.dumps(responseData)

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

def gen_summary_json(watch):
    json_data = {
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
        'dev_pass' : _summary_dev_pass()
    }

    if json_data.has_key(watch):
        return json_data[watch]

    return {}

