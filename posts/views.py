from django.shortcuts import render, redirect
from general.models import Posts
from .forms import PostsForm
from general.models import User
from scripts import login_required


# Create your views here.
@login_required
def search_posts(request):
    context = {'posts_to_show': []}

    for post in Posts.objects.order_by('-id'):
        user = User.objects.get(id=post.author_p_id)
        context['posts_to_show'].append(
            [post.title, post.place, post.full_text, user.first_name, user.second_name, user.id])

    # if request.method == "POST":
    #     if request.POST.get('Find'):
    #         form =

    return render(request, 'search_posts.html', context)


@login_required
def create_posts(request):
    error = ''

    if request.method == "POST":
        posts = Posts()
        form = PostsForm(request.POST)
        if form.is_valid():
            posts.title = form.data['title']
            posts.place = form.data['place']
            posts.full_text = form.data['full_text']
            posts.author_p = User.objects.get(session=request.COOKIES['session'])

            posts.save()
            return redirect('/search_posts')
        else:
            error = 'The form is filled out incorrectly'

    form = PostsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'create_posts.html', data)
