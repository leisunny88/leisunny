"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views
app_name = 'account'
urlpatterns = [
    # url(r'^login/$', views.user_login, name="user_login"),
    url(r'^login/$', auth_views.LoginView.as_view(), name='user_login'),
    url(r'^new-login/$', auth_views.LoginView.as_view(), {"template_name": "account/login.html"}),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='user_logout'),
    url(r'^new-logout/$', auth_views.LogoutView.as_view(), {"template_name": "account/logout.html"}),
    url(r'^register/$', views.register, name='user_register'),

]
