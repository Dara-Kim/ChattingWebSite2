# chat/urls.py
from django.urls import path

from . import views

app_name = "logInOut"

urlpatterns = [
    path('', views.login, name='index'),
    path('chat/index/', views.index_, name='index'),
    path("login/", views.login, name="login"),
    path("chat/create_account/", views.create_account, name="create_account"),
    path("chat/create_room/", views.create_room, name="create_room"),
    path("chat/room/", views.rooms, name="room"),
]