
from bottle import run, route, template, static_file

@route('/')
def index():
    return template('index')


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root="./")

@route('/forum')
def display_forum():
    forum_id = request.query.id
    forum_page = request.query.page
    return "id: " + forum_id + "<br>" + "page: " + forum_page

if  __name__=='__main__':
    run()
