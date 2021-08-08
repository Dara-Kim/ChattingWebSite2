import json
import os

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.


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

        req_data = {}

        with open("./logInOut/db/idpw.json", 'r') as jsonfile:
            idpw = json.load(jsonfile)

            if user_id in idpw.keys():
                req_data["stat"] = 0
                req_data["errmsg"] = "이미 존재하는 ID 입니다"
            elif len(pw) < 6:
                req_data["stat"] = 0
                req_data["errmsg"] = "비밀번호는 6자 이상 설정해 주세요"
            else:
                req_data["stat"] = 1
                req_data["errmsg"] = ""

        return JsonResponse(req_data)
    else:
        return render(req, "logInOut/create_account.html")