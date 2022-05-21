from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_posts),
    path('<int:pk>', views.ProfileDetailView.as_view(), name='profile-detail')
]