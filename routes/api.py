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

@route('/api/summary/:target/:query', method='GET')
def api_summary(target, query):
    responseData = gen_summary_json(target, query)

    response.content_type = 'application/json'
    return json.dumps(responseData)

def _summary_dev_send():
    """統計開發單位送出審核案件數

        以開發單位提列環評案件數，得知有哪些營利單位或政府單位，對環境異動有極大影響作用。
    """

    sql_script = """
        SELECT devunit, count(*) count FROM details
        WHERE devunit != ""
        GROUP BY devunit ORDER BY count DESC
        LIMIT 10
    """
    cur.execute(sql_script)
    row = cur.fetchall()

    return row

def _summary_dev_pass():
    """統計開發單位送出審核案件通過數

        總計營利單位或政府單位通過提列環評案件。
    """

    sql_script = """
        SELECT devunit, count(*) count FROM details
        WHERE devunit != "" AND TRIM(examinestatus) in (
            '審核修正通過',
            '審核通過',
            '有條件通過環境影響評估',
            '通過環境影響評估審查'
        )
        GROUP BY devunit ORDER BY count DESC
        LIMIT 10
    """

    cur.execute(sql_script)
    row = cur.fetchall()
    return row

def gen_summary_json(target,query):
    json_data = {
        'city': {
            'area': [
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
            ]
        },
        'dev': {
            'send' : _summary_dev_send(),
            'pass' : _summary_dev_pass()
        }
    }

    if json_data.has_key(target) and json_data[target].has_key(query):
        return json_data[target][query]

    return {}

