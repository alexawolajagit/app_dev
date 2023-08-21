from django.urls import path
from . import views

#write urls here
urlpatterns =[
    path('', views.home, name='home'),
]