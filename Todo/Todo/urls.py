"""Todo URL Configuration

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
from django.views.generic import TemplateView 
from todolist.views import Login
from todolist.views import Register
from django.conf.urls import include, url
from todolist.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),

    path('login/check/', Login.as_view(), name='login-check'),    # 还没写完的登录接口
    path('register/check/', Register.as_view(), name='register-check'),  # 还没写完的登录接口
    path('info/', Info.as_view()),
    # url(r'^publish/', views.publish),
    path('del/', Del.as_view()),
    path('edit/',Edit.as_view()),
    path('flag/', Flag.as_view()),
    # path('login/', views.Login)
]
