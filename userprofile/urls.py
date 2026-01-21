from . import views
from django.urls import path

urlpatterns = [
    path('', views.profile, name='user_profile'),
]
