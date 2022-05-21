from django.shortcuts import render, redirect
from general.models import Posts
from django.utils import timezone
from .forms import PostsForm
from general.models import User, Vote
from scripts import login_required
from django.views.generic import DetailView
import ast
import re


# Create your views here.
@login_required
def search_posts(request):
    context = {'posts_to_show': []}

    for post in Posts.objects.order_by('-id'):
        user = User.objects.get(id=post.author_p_id)

        context['posts_to_show'].append(
            [post, user])

    user = User.objects.get(session=request.COOKIES['session'])
    context['cur'] = user



    return render(request, 'search_posts.html', context)


@login_required
def create_posts(request):
    error = ''

    if request.method == "POST":
        posts = Posts()
        form = PostsForm(request.POST)
        if form.is_valid():
            vote = Vote()

            user = User.objects.get(session=request.COOKIES['session'])
            posts.title = form.data['title']
            posts.place = form.data['place']
            posts.full_text = form.data['full_text']
            posts.author_p = user
            vote.post_id = posts.id
            vote.user_1_id = user.id

            posts.save()
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


class ProfileDetailView(DetailView):
    model = User

    template_name = 'profile_guest.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    context_object_name = 'article'
