from django.shortcuts import render
from scripts import login_required
from general.models import User, Posts


# Create your views here.

@login_required
def profile_page(request):
    user = User.objects.get(session=request.COOKIES['session'])
    context = {'name': user.username, 'first_name': user.first_name, 'second_name': user.second_name, 'age': user.age,
               'gender': user.gender, 'users_posts': []}
    posts = Posts.objects.filter(author_p_id=user.id)
    for i in posts:
        context['users_posts'].append([i.title, i.place, i.full_text])
    return render(request, 'profile.html', context)


def index_page(request):
    context = {}

    return render(request, 'index.html', context)
