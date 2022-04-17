"""road_love URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
import general.views
import posts.views
import registration.views
from general.views import profile_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', general.views.index_page),
    path('create_post/', posts.views.create_poll_page),
    path('login/', registration.views.login_page),
    path('signup/', registration.views.sign_up_page),
    path('profile/', profile_page),
    path('poll/', posts.views.poll_page),
    path('search_post/', posts.views.search_poll),
    path('logout/', registration.views.logout),
    path('access_denied/', registration.views.access_denied),
    path('profile_filling/', registration.views.profile_filling),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

