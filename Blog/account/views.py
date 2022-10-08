from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import LoginSerializer
from django.contrib.auth.models import User
from .forms import LoginForm


class LoginView(APIView):

    def get(self, request, format=None):
        content = {
            'user': str(request.user)
        }
        return Response(content)

    def post(self, request, format=None):
        form = LoginForm(data=request.data)
        print(form.is_valid())
        print(form['username'])
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('success')
                return HttpResponse('Disabled User')
            return HttpResponse('Invalid Login')
        else:
            return HttpResponse('failed Login')

class LogoutView(APIView):

    def get(self, request, format=None):
        logout(request)
        return HttpResponse('successfully logged out')
