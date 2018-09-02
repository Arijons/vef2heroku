from sys import argv

import bottle
from bottle import*
bottle.debug(True)

from bottle import route, run, error
#a
#byrta strenginn halló heimur
@route("/hello")
def hello():
    return "Hello World!"

@route("/hello/<name>")
def greet(name="Strange"):
    return template("Hello {{name}}, how are you?", name=name)


@error(404)
def custome(error):
    return "þetta er villa settu, sláðu inn rétta rót"




#b
#Útfæra vefforrit í bottlepy
@route("/sida")
def sida():
    return "aðalsíða"

@route("/sida/undirsida1")
def us1():
    return "undirsida 1"

@route("/sida/undirsida2")
def us2():
    return "undirsida 2"

@route("/sida/undirsida3")
def us3():
    return "undirsida 3"

@error(404)
def custom404(error):
    return "sláðu inn rétta rout"

run(host="localhost", port=8080, debug=True)














