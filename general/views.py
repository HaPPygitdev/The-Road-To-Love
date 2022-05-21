from django.shortcuts import render, redirect
from scripts import login_required
from general.models import User, Posts
from .forms import UsersForm
from posts.forms import PostsForm
from django.http import HttpResponseRedirect


# Create your views here.

@login_required
def profile_page(request):
    user = User.objects.get(session=request.COOKIES['session'])

    context = {'name': user.username, 'first_name': user.first_name, 'second_name': user.second_name, 'age': user.age,
               'gender': user.gender, 'coordinate': user.coordinate, 'description': user.description, 'users_posts': []}

    posts = Posts.objects.filter(author_p_id=user.id)
    for i in posts:
        context['users_posts'].append([i.title, i.place, i.full_text])
    cor_current = user.coordinate.split('<br>')
    context['cor_current'] = "https://catalog.api.2gis.com/3.0/items?q=cafe&sort_point=" + str(
        cor_current[0]) + "," + str(cor_current[1]) + "&key=ruswpk8061"

    return render(request, 'profile.html', context)


def index_page(request):
    context = {}

    return render(request, 'index.html', context)


@login_required
def edit_profile_page(request):
    error = ''

    if request.method == 'POST':
        user = User.objects.get(session=request.COOKIES['session'])
        form = UsersForm(request.POST)
        if form.is_valid():
            user.description = form.data['description']

            user.save()
            return redirect('/profile')
        else:
            error = 'The form is filled out incorrectly'

    form = UsersForm()

    context = {
        'form': form,
        'error': error
    }

    return render(request, 'edit_profile.html', context)
