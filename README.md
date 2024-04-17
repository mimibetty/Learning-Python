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

RUN CMD: 
Start a New Django Project:   django-admin startproject webtest(name project)
Change Directory to the New Project: cd webtest
Start a New App within the Django Project: python manage.py startapp hello



** Run the Django Development Server: python manage.py runserver
if you want your web run at different port(ex 7474):  python manage.py runserver 7474


then create an app name home74,  python manage.py startapp home74
declare app,   go into webtest/settings.py,  modify install_app 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home74',
]

then update : python manage.py migrate 

learn how to test a page: go into home74/test 
run cmd : python manage.py test home74



