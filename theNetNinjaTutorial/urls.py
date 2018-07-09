
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about), # '$' means this is the end, nothing after (find expression)
    path('', views.homepage), # homepage
]
