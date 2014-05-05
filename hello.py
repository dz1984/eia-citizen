from bottle import route, template, jinja2_view as view

'''
@route('/hello')
@route('/hello/<name>')
def hello(name='world'):
	return template('<b>Hello {{name}}</b>!', name=name)
'''

@route('/')
@view('home.html')
def home():
	return {}

'''
@route('/templates/base')
@jinja2_view('base.html')
def templates_base():
	return {}
'''
