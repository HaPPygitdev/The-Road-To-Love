from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import PostsForm
from general.models import User, Vote, Message, Posts
from scripts import login_required
from django.views.generic import DetailView
import json
import requests


# Create your views here.
@login_required
def search_posts(request):
    error = ''
    context = {'posts_to_show': []}

    user = User.objects.get(session=request.COOKIES['session'])
    context['cur'] = user

    if request.method == "POST":
        vote = Vote.objects.get(post_id=request.POST.get('Find'))

        vote.user_2_id = user.id
        vote.save()
        return redirect('/responds')

    for post in Posts.objects.order_by('-id'):
        user2 = User.objects.get(id=post.author_p_id)

        vote = Vote.objects.get(post_id=post.id)

        if vote.user_1_id == vote.user_2_id:
            context['posts_to_show'].append([post, user2])

    return render(request, 'search_posts.html', context)


@login_required
def create_posts(request):
    error = ''

    if request.method == "POST":
        posts = Posts()
        form = PostsForm(request.POST)
        if form.is_valid():
            user = User.objects.get(session=request.COOKIES['session'])
            posts.title = form.data['title']
            posts.place = form.data['place']
            posts.full_text = form.data['full_text']
            posts.author_p = user

            posts.save()
            vote = Vote()

            vote.post_id = posts.id
            vote.user_1_id = user.id
            vote.user_2_id = user.id

            vote.save()

            return redirect('/search_posts')
        else:
            error = 'The form is filled out incorrectly'

    form = PostsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'create_posts.html', data)


def responds_view(request):
    context = {'posts_to_show_1': [], 'posts_to_show_2': []}

    if request.method == "POST":
        if request.POST.get('Reject'):
            vote1 = Vote.objects.get(post_id=request.POST.get('Reject'))

            vote1.user_2_id = vote1.user_1_id
            vote1.save()

        if request.POST.get('Accept'):
            vote1 = Vote.objects.get(post_id=request.POST.get('Accept'))

            post_cur = Posts.objects.get(id=vote1.post_id)

            user1 = User.objects.get(id=vote1.user_1_id)
            user2 = User.objects.get(id=vote1.user_2_id)

            coordinate_1 = user1.coordinate.split('<br>')
            coordinate_2 = user2.coordinate.split('<br>')

            mid = [str(float(min(coordinate_1[0], coordinate_2[0])) + abs(
                float(coordinate_1[0]) - float(coordinate_2[0])) / 2),
                   str(float(min(coordinate_1[1], coordinate_2[1])) + abs(
                       float(coordinate_1[1]) - float(coordinate_2[1])) / 2)]

            message = Message()

            message.user_1_id = user1.id
            message.user_2_id = user2.id
            message.middle = "https://catalog.api.2gis.com/3.0/items?q=" + str(post_cur.place) + "&sort_point=" + str(
                mid[0]) + "," + str(mid[1]) + "&key=ruswpk8061"

            message.save()

            return redirect('/message')

    user = User.objects.get(session=request.COOKIES['session'])

    for vote in Vote.objects.filter(user_1_id=user.id):
        if vote.user_1_id != vote.user_2_id:
            post = Posts.objects.get(id=vote.post_id)
            usr = User.objects.get(id=vote.user_2_id)

            context['posts_to_show_1'].append([post, user, usr])

    for vote in Vote.objects.filter(user_2_id=user.id):
        if vote.user_2_id != vote.user_1_id:
            post2 = Posts.objects.get(id=vote.post_id)
            usr = User.objects.get(id=post2.author_p_id)

            context['posts_to_show_2'].append([post2, usr])

    return render(request, 'responds.html', context)


class ProfileDetailView(DetailView):
    model = User

    template_name = 'profile_guest.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    context_object_name = 'article'


def message_view(request):
    context = {'messages': [], 'places': []}

    if request.method == 'POST':
        li = request.POST.get('Fin').split('|')
        message = Message.objects.get(id=li[2])

        message.place_name = li[0]
        message.place_address = li[1]

        message.save()
        message2 = Message()

        message2.user_1_id = message.user_2_id
        message2.user_2_id = message.user_1_id
        message2.middle = message.middle
        message2.place_name = message.place_name
        message2.place_address = message.place_address

        message2.save()

    user = User.objects.get(session=request.COOKIES['session'])
    for message in Message.objects.filter(user_1_id=user.id):
        if not message.place_name:
            response = requests.get(message.middle)
            todos = json.loads(response.text)

            for i in todos['result']['items']:
                context['places'].append([i, message.id])
        else:
            user2 = User.objects.get(id=message.user_2_id)
            context['messages'].append([message, user2])

    return render(request, 'message.html', context)
