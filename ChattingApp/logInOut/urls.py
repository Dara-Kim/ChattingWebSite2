# chat/urls.py
from django.urls import path

from . import views

app_name = "logInOut"

urlpatterns = [
    path('index/', views.index, name='index'),
    path("", views.login, name="login"),
    path("create_account", views.create_account, name="create_account")
]