"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from Django import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include('posts.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^googly/',include('googly.urls',namespace='googly')),
    url(r'^twitty/',include('twitty.urls',namespace='twitty')),
    url(r'^gitty/',include('gitty.urls',namespace='gitty')),
    url(r'^api/',include('api.urls',namespace='api')),
    url(r'^accounts/',include('allauth.urls')),

]
# 3ashan ata3araf el el two files (Media & Static)
if settings.DEBUG:
	urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)