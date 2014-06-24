# -.- encoding: utf-8 -.-
#
# 靜態檔案
#
import os
from bottle import route, static_file

OPENSHIFT_REPO_DIR = os.environ['OPENSHIFT_REPO_DIR']
VIEWS_DIR = OPENSHIFT_REPO_DIR + 'wsgi/views/'

@route('/css/<filename>')
def css(filename):
    return static_file(filename, root = VIEWS_DIR + 'css')

@route('/js/<filename>')
def js(filename):
    return static_file(filename, root= VIEWS_DIR + 'js')
