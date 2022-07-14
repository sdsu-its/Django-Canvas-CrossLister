
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('app/', views.app, name="app"),
    path('run/', views.run, name="run"),
    path('confirm/', views.confirm, name="confirm"),
    path('result/', views.result, name="result"),

]