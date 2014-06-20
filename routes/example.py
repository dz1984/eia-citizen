from bottle import route, template, jinja2_view as view


@route('/example')
@view('example.html')
def example_index():
    return {}

@route('/example/dev_pass')
@view('layout/example_base.html')
def example_dev_pass():
    return {}

