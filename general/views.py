from django.shortcuts import render, redirect
from scripts import login_required
from general.models import User, Posts
from .forms import UsersForm
from django.core.files.storage import FileSystemStorage


# Create your views here.

@login_required
def profile_page(request):
    user = User.objects.get(session=request.COOKIES['session'])

    context = {'name': user.username, 'first_name': user.first_name, 'second_name': user.second_name, 'age': user.age,
               'gender': user.gender, 'coordinate': user.coordinate, 'description': user.description,
               'photo': user.photo, 'users_posts': []}

    posts = Posts.objects.filter(author_p_id=user.id)
    for i in posts:
        context['users_posts'].append([i.title, i.place, i.full_text])

    return render(request, 'profile.html', context)


def index_page(request):
    context = {}

    return render(request, 'index.html', context)


@login_required
def edit_profile_page(request):
    error = ''
    context = {}
    if request.method == 'POST':
        user = User.objects.get(session=request.COOKIES['session'])
        form = UsersForm(request.POST)
        if request.FILES:
            file = request.FILES['myfile1']
            fs = FileSystemStorage()
            # сохраняем на файловой системе
            filename = fs.save(file.name, file)
            # получение адреса по которому лежит файл
            file_url = fs.url(filename)

            user.photo = file_url

            user.save()

        if form.is_valid():
            user.description = form.data['description']

            user.save()
            return redirect('/profile')
        else:
            error = 'The form is filled out incorrectly'

    form = UsersForm()

    context['form'] = form
    context['error'] = error

    return render(request, 'edit_profile.html', context)
