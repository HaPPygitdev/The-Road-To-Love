from django.shortcuts import render
from scripts import login_required
from general.models import User, Poll


# Create your views here.

@login_required
def profile_page(request):
    user = User.objects.get(session=request.COOKIES['session'])
    context = {'name': user.username, 'users_polls': []}
    poll = Poll.objects.filter(author_id=user.id)
    for i in poll:
        context['users_polls'].append("<a href='../poll/?id=" + str(i.id) + "'>" + i.title + "</a>")
    return render(request, 'profile.html', context)


def index_page(request):
    context = {}

    return render(request, 'index.html', context)
