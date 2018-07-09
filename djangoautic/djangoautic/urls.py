
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')), # when this url is requested, look up articles/urls.py
    path('about/', views.about), # '$' means this is the end, nothing after (find expression)
    path('', views.homepage), # homepage
]
