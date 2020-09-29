from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Greeting
from django.views import generic
from django.views.generic import TemplateView
from django.urls import path

from . import views

# Create your views here.

""" class IndexView(TemplateView):
    template_name = 'babydragon/index.html' """

def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def donate(request):
    return render(request, "donate.html")

""" def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>') """


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
