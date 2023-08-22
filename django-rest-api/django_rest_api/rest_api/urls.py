from django.urls import path
from . import views

#url paths
urlpatterns = [
    path('', views.getApi),
    path('post/', views.postApi),
]