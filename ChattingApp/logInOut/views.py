import json
import os

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
from logInOut.models import Report


def index(request):
    return HttpResponse("Hello, world. You're at the login page.")


def index_(request):
    return render(request, "logInOut/index.html")


def login(req):
    if req.is_ajax and req.method == "POST":
        data = json.loads(req.body)
        user_id = data.get("user_id")
        pw = data.get("pw")

        with open("./logInOut/db/idpw.json", 'r') as jsonfile:
            idpw = json.load(jsonfile)

            if user_id in idpw:
                if idpw[user_id] == pw:
                    return JsonResponse({"stat": 1})
            else:
                return JsonResponse({"stat": 0})

        return JsonResponse({"stat": 0})
    else:
        return render(req, "logInOut/login.html")


def create_account(req):
    if req.is_ajax and req.method == "POST":
        data = json.loads(req.body)
        user_id = data.get("user_id")
        pw = data.get("pw")

        with open('./logInOut/db/idpw.json', 'r') as r:
            jsonfile = json.load(r)
            req_data = {}

            if user_id in jsonfile.keys():
                req_data["stat"] = 0
                req_data["errmsg"] = "이미 존재하는 ID 입니다"
            elif len(pw) < 6:
                req_data["stat"] = 0
                req_data["errmsg"] = "비밀번호는 6자 이상 설정해 주세요"
            else:
                req_data["stat"] = 1
            if req_data["stat"] == 1:
                req_data[user_id] = pw
                with open('./logInOut/db/idpw.json', 'w') as w:
                    json.dumps(req_data, jsonfile)

        return JsonResponse(req_data)
    else:
        return render(req, "logInOut/create_account.html")


def enter_room(req):
    if req.is_ajax and req.method == "POST":
        data = json.loads(req.body)
        room_id = data.get("user_id")

        with open("./logInOut/db/rooms.json", 'r') as jsonfile:
            room = json.load(jsonfile)

            if room_id in room:
                return JsonResponse({"stat": 1})
            else:
                return JsonResponse({"stat": 0})

        return JsonResponse({"stat": 0})
    else:
        return render(req, "room.html")


def create_room(req):
    if req.is_ajax and req.method == "POST":
        data = json.loads(req.body)
        room_id = data.get("room_id")

        with open('./logInOut/db/rooms.json', 'r') as r:
            jsonfile = json.load(r)
            req_data = {}
            chat_data = {}

            if room_id in jsonfile.keys():
                req_data["stat"] = 0
                req_data["errmsg"] = "이미 존재하는 룸 입니다"
            elif len(room_id) < 3:
                req_data["stat"] = 0
                req_data["errmsg"] = "채팅방 이름은 3자 이상 설정해 주세요"
            else:
                req_data["stat"] = 1
            if req_data["stat"] == 1:
                #req_data[room_id] = chat_data
                with open('./logInOut/db/rooms.json', 'w') as w:
                    json.dumps(req_data, jsonfile)

        return JsonResponse(req_data)
    else:
        return render(req, "logInOut/rooms.html")


def chat(req, room_id, user_id, talk):
    if req.is_ajax and req.method == "POST":
        data = json.loads(req.body)

        with open('./logInOut/db/rooms.json', 'w') as w:
            jsonfile = json.load(w)
            req_data = {}
            # req_data["room_id"][n][시간][0] = user_id
            # req_data["room_id"][n][시간][0] = talk
            json.dumps(req_data, jsonfile)

        return JsonResponse(req_data)
    else:
        return render(req, "logInOut/rooms.html")
