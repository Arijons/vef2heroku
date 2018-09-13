
from bottle import run, route, template, static_file

@route('/')
def index():
    return template('index')


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root="./")

if  __name__=='__main__':
    run(reloader=True, debug=True)
