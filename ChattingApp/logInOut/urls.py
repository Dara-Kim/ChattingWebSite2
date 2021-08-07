from django.urls import path

from . import views

app_name = 'logInOut'

urlpatterns = [
    path('', views.index, name='index'),
]