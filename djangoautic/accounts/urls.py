# https://docs.djangoproject.com/en/2.0/ref/urls/
from django.urls import path, re_path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
]
