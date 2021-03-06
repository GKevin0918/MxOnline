# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic import View

from .models import UserProfile
from .forms import LoginForm, RegisterForm


# Create your views here.
class CustomBakend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html", {})


class LoginView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", " ")
            pass_word = request.POST.get("password", " ")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, "index.html")
            else:
                return render(request, "login.html", {"msg": "用户名或者密码不正确"})
        else:
            return render(request, "login.html", {"login_form": login_form})

            # def user_login(request):
            #     if request.method == "POST":
            #         user_name = request.POST.get("username", " ")
            #         pass_word = request.POST.get("password", " ")
            #         user = authenticate(username=user_name, password=pass_word)
            #         if user is not None:
            #             login(request, user)
            #             return render(request, "index.html")
            #         else:
            #             return render(request, "login.html", {"msg": "用户名或者密码不正确"})
            #     elif request.method == "GET":
            #         return render(request, "login.html", {})
