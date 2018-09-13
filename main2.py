
down vote
accepted
I usually use the following

import bottle
from bottle import route, run, template, BaseTemplate, static_file

app = bottle.default_app()
BaseTemplate.defaults['get_url'] = app.get_url  # reference to function

@route('/')
def index():
    return template('mytemplate')


@route('/static/<filename:path>', name='static')
def serve_static(filename):
    return static_file(filename, root='static')

run(host='localhost', port=8080)

