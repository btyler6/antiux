from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Donation
from .forms import DonationForm
from django.views import generic
from django.views.generic import TemplateView
from django.urls import path
from django.shortcuts import redirect

from . import views

# Create your views here.

""" class IndexView(TemplateView):
    template_name = 'babydragon/index.html' """

def index(request):
    return render(request, "hello/index.html")

def donate(request):
    return render(request, "hello/donate.html")

""" def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>') """

def donatehere(request):
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = DonationForm()
    return render(request, 'hello/donatehere.html', {'form': form})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
