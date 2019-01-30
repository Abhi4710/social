"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^social/home$', views.home, name='Index'),
    url(r'^social/user_login$', views.user_login, name='user_login'),
    url(r'^social/user_profile$', views.profile, name='user_profile'),
    url(r'^social/user_logout$', views.user_logout, name='user_logout'),
    url(r'^social/user_register$', views.user_register, name='user_register'),
    url(r'^social/edit_profile$', views.user_edit, name='edit_profile'),
    url(r'^social/user_delete$', views.user_del, name='user_delete'),
    url(r'^social/change_pass$', views.pass_change, name='change_pass'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
