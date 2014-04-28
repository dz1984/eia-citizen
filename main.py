#!../bin/python
# -.- encoding: utf-8 -.-

from bottle import route, run, template, TEMPLATE_PATH

# 載入所有的 request 處理程式
import admin
import hello

run(host='localhost', port=8080)
