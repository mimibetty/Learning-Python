# Learning-Python
Learning framework in python  and some application 

https://topdev.vn/blog/django-de-hon-flask/
day 1: 15/4/2024

for flask :

from flask import Flask
app = Flask("my website")

@app.route("/")
def hello_world():
    return "hahaaa world"

@app.route("/hello/<string:name>")
def hello(name):
    return "Hello {}".format(name)



RUN CMD: 

$env:FLASK_APP = "hello.py"
flask run




Django