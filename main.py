#!../bin/python
# -.- encoding: utf-8 -.-

from bottle import route, run, template, TEMPLATE_PATH

#from jinja2 import Environment, PackageLoader
#env = Environment(loader=PackageLoader('hello', 'templates'))
TEMPLATE_PATH.append("./templates")

# 載入所有的 request 處理程式
import hello

run(host='localhost', port=8080)
