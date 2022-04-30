from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostsForm


# Create your views here.
def search_posts(request):
    posts = Posts.objects.all()
    return render(request, 'search_posts.html', {'posts': posts})


def create_posts(request):
    error = ''

    if request.method == "POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/profile')
        else:
            error = 'Форма была неверной'

    form = PostsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'create_posts.html', data)