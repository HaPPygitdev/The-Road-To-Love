import string
from urllib import response
from django.shortcuts import render

from registration.forms import LoginForm
from registration.forms import SignUpForm, ProfileSignUpForm
from general.models import User
from django.http import HttpResponseRedirect

import hashlib
from random import choice

from scripts import login_required


def login_page(request):
    context = {}
    fail = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.data['username'].strip()
            password = form.data['password'].strip()

            try:
                user = User.objects.get(username=username)

                if user.password_hash == hashlib.sha256((password + user.salt).encode('utf-8')).hexdigest():
                    response = HttpResponseRedirect('/profile/')
                    session = ''.join(choice(string.hexdigits) for _ in range(30))
                    user.session = session
                    user.save()
                    response.set_cookie('session', session)
                    return response
                else:
                    fail = 'Wrong password'
            except:
                fail = 'User not found'

    context['form'] = LoginForm()
    context['fail'] = fail
    return render(request, 'login.html', context)


def sign_up_page(request):
    context = {}
    fail = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.data['username'].strip()
            password = form.data['password'].strip()
            confirm_password = form.data['confirm_password'].strip()

            user = User.objects.filter(username=username)
            if not user:
                if password == confirm_password:
                    salt = ''.join(choice(string.hexdigits) for _ in range(30))
                    user = User(username=username,
                                password_hash=hashlib.sha256((password + salt).encode('utf-8')).hexdigest())
                    user.salt = salt
                    response = HttpResponseRedirect('/profile_filling/')
                    session = ''.join(choice(string.hexdigits) for _ in range(30))
                    user.session = session
                    user.save()
                    response.set_cookie('session', session)
                    return response

                else:
                    fail = 'Passwords must be the same'
            else:
                fail = 'Such username have already created'

    context['form'] = SignUpForm()
    context['fail'] = fail
    return render(request, 'sign_up.html', context)


def profile_filling(request):
    context = {}
    fail = ''
    if request.method == 'POST':
        form = ProfileSignUpForm(request.POST)

    context['form'] = ProfileSignUpForm()
    context['fail'] = fail
    return render(request, 'profile_filling.html', context)


@login_required
def logout(request):
    user = User.objects.get(session=request.COOKIES['session'])
    user.session = ''
    user.save()

    response = render(request, 'logout.html')
    response.delete_cookie('session')

    return response


def access_denied(request):
    return render(request, 'access_denied.html')
