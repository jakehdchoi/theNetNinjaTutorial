
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings # importing from settings.py
from articles import views as article_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about), # '$' means this is the end, nothing after (find expression)
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')), # when this url is requested, look up articles/urls.py
    path('', article_views.article_list, name='home'), # homepage
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
