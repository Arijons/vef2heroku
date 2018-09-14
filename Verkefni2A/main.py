# -*- coding: utf-8 -*-

from bottle import Bottle, template

app = Bottle()



@app.route('/')
def index():
    """Home page"""

    info = {'title': 'Welcome Home!',
            'content': 'Hello World'
            }

    return template('simple.tpl', info)


@app.route('/<name>')
def greet(name='Stranger'):
    return "Hello " + name


#@app.route('/1/')
#def index():
   # return <h1>linkur1</h1>

if __name__ == '__main__':
    app.run()