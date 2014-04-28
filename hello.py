from bottle import route, template, jinja2_view

@route('/hello')
@route('/hello/<name>')
def hello(name='world'):
	return template('<b>Hello {{name}}</b>!', name=name)

@route('/')
def home():
	return 'Home'

@route('/templates/base')
@jinja2_view('base.html')
def templates_base():
	return {}
