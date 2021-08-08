# chat/urls.py
from django.urls import path

from . import views

app_name = "logInOut"

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index_, name='index'),
    path("login/", views.login, name="login"),
    path("create_account/", views.create_account, name="create_account")
]