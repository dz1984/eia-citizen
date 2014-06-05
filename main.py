#!../bin/python
# -.- encoding: utf-8 -.-
#
# Bottle 服務啟動程式
#

RELEASE = False
WITH_ADMIN = True


import os,sys

sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'libs'))

# 載入所有的 request 處理程式
import routes

if WITH_ADMIN:
    import admin

# 啟動服務
from bottle import run

if RELEASE:
    # 上線環境啟動方式
    #print('啟動上線環境')
    run(host='localhost', port=8080)
else:
    # 開發環境啟動方式
    # reloader: *.py 檔案有更動時重新啟動服務
    #    debug: 觀察 HTTP Request, 以及關閉版型快取
    #print('啟動開發環境')
    run(host='localhost', port=8080, reloader=True, debug=True)
