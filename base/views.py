from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1> Home page goes there !!!<h1>')


def room(request):
    return HttpResponse('<h1>Room page there !!!!</h1>')


def about(request):
    return HttpResponse('<h1>About page goes there !!!</h1>')
