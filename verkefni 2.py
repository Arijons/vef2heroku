from bottle import route, run, error

@route("/register")
def register():
    return "<h1>On the register page</h1>"

@route("/article/<id>")
def article(id):
    return "<h1>You are viewing article " + id + "</h1>"

@route("/page/<id>/<name>")
def page(id, name):
    return "<h1>You are viewing page " + id + " with the name of " + name + "</h1>"

# A liður

@route("/bls/<tala>/<nafn>/<dagsetning>")
def bls (tala,nafn,dagsetning):
    return "<h1> Þú ert að lesa þessa grein á bls " + tala + " og var skrifuð á þessum degi " + dagsetning + " og greinin fjallar um " + nafn + "</h1>"



@error(404)
def costume404(error):
    return "sláðu inn rétta route"

if __name__ == "__main__":
    run(debug=True, reloader=True)
