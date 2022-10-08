from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import LoginSerializer, RegistrationSerializer
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm


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

class RegistrationView(APIView):

    def get(self, request, format=None):
        user_form = RegisterForm()
        return HttpResponse(user_form)

    def post(self, request, format=None):
        register = RegisterForm(data=request.data)
        if register.is_valid():
            new_user = register.save(commit=False)
            new_user.set_password(register.cleaned_data['password'])
            new_user.save()
            return HttpResponse('Successfully registered')
        else:
            return HttpResponse('Invalid Register')
