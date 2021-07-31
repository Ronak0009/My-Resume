from django.urls import path,re_path
from .views import *
from django.contrib import admin



urlpatterns = [
    path('home/<int:no>', home_view),
    path('home-horizontal/<int:no>',home_horizontal_view),
    path('slider/',home_slider),
    path('nav/',navbar),

]
