from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("donate/", views.donate, name='donate'),
    path("db/", views.db, name="db"),
    path("donatehere/", views.donatehere, name='donatehere'),                
    path("thanks/", views.thanks, name="thanks"),
]