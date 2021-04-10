
"""Accounts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# gloabl import
from django.urls import path, include
from django.conf.urls import url

#local import
from .views import *

urlpatterns = [
    path(r'', include('allauth.urls')),
    # url(r'^signup/$', SignupView.as_view(), name='account_signup'),
    url(r'^login/$', LoginView.as_view(), name='account_login'),
    url(r'^logout/$', LogoutView.as_view(), name='account_logout'),
]