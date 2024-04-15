from flask import Flask
app = Flask("my website")

@app.route("/")
def hello_world():
    return "hahaaa world"

@app.route("/hello/<string:name>")
def hello(name):
    return "Hello {}".format(name)
