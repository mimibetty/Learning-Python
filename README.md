# Learning-Python
Learning framework in python  and some application 

https://topdev.vn/blog/django-de-hon-flask/
source : https://www.youtube.com/watch?v=_D5WGp2chtk&list=PL33lvabfss1z8GYxjyMulCnhcYGk5ah8P&index=5&ab_channel=Kteam
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


Lesson 4 :
 create 2 file html base and home
in home, use base as a template 
code : {% extends "pages/base.html" %}

Lesson 5: use bootstrap 

notice: 
The error you're encountering indicates that the staticfiles tag library is not found or not registered. This might be due to a change in how Django handles static files in newer versions. In Django 3.x and earlier, you used {% load staticfiles %}, but since Django 3.1, this has been simplified to {% load static %}.

To fix the error, replace the line:
{% load staticfiles %}
with:
{% load static %}


result : 
![image](https://github.com/mimibetty/Learning-Python/assets/74227789/5fc6aefb-984d-4faf-b999-0f9335aee906)


Lesson 6: finish first blog 
![image](https://github.com/mimibetty/Learning-Python/assets/74227789/ccbc9e67-305e-4313-b5a5-8bd8132941dd)
