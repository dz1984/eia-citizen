from bottle import route, template, jinja2_view as view


@route('/example')
@view('example.html')
def example_index():
    return {}


