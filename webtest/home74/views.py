from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    response = HttpResponse()
    response.writelines("<h1> Xin chào mimibetty </h1>")
    response.writelines("<p> test app home 74 </p>")
    return response