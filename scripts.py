from urllib import request
from django.http import HttpResponseRedirect
from general.models import User


def login_required(views_function):
    def wrapper(request, *args, **kwargs):
        if 'session' in request.COOKIES:
            user = User.objects.filter(session=request.COOKIES['session'])
            if len(user) == 1:
                return views_function(request, *args, **kwargs)
        return HttpResponseRedirect('/access_denied')
    
    return wrapper
