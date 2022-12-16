from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
import requests
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Account
from django.contrib.auth.hashers import make_password

import json


URL = "http://127.0.0.1:8001"

def get_token():
    # Get auth Token
    url = f"{URL}/api/auth/"
    response = requests.post(url, data={'username': 'mafiqamir',
                                        'password': 'password'})
    return response.json()

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #log user in
            login(request, user)
            return redirect('channels:myChannel')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        url = f"{URL}/api/users_list"
        token = get_token()
        header = {'Authorization': f'Token {token}'}
        response = requests.get(url, headers=header)
        data = response.json()

        for datas in data:
            trainee_id = datas['id']
            pwd = datas['Password']
            encrypted = make_password(pwd, salt=None, hasher='default')

            new_user = User(
                id=trainee_id,
                email=datas['Email'],
                username=datas['Username'],
                password=encrypted
            )
            new_user.save()

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('channel:myChannel')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login2.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')