# -.- encoding: utf-8 -.-
#
# 靜態檔案
#

from bottle import route, static_file

@route('/css/<filename>')
def css(filename):
	return static_file(filename, root='./css')

@route('/js/<filename>')
def js(filename):
	return static_file(filename, root='./js')
