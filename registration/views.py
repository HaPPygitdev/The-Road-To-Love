import string
from urllib import response
from django.shortcuts import render

from registration.forms import LoginForm
from registration.forms import SignUpForm
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
            coordinate = form.data['coordinate'].strip()

            try:
                user = User.objects.get(username=username)

                if user.password_hash == hashlib.sha256((password + user.salt).encode('utf-8')).hexdigest():
                    response = HttpResponseRedirect('/profile/')
                    session = ''.join(choice(string.hexdigits) for _ in range(30))
                    user.session = session
                    user.coordinate = coordinate
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
            first_name = form.data['first_name'].strip()
            second_name = form.data['second_name'].strip()
            age = form.data['age'].strip()
            gender = form.data['gender'].strip()
            coordinate = form.data['coordinate'].strip()

            user = User.objects.filter(username=username)
            if not user:
                if password == confirm_password:
                    salt = ''.join(choice(string.hexdigits) for _ in range(30))
                    user = User(username=username,
                                password_hash=hashlib.sha256((password + salt).encode('utf-8')).hexdigest(),
                                first_name=first_name, second_name=second_name, age=age, gender=gender)
                    user.salt = salt
                    response = HttpResponseRedirect('/profile/')
                    session = ''.join(choice(string.hexdigits) for _ in range(30))
                    user.session = session
                    user.coordinate = coordinate
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
