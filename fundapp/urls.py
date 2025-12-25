"""crowdfund URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('Login', views.Login,name='Login'),
    path('homepage', views.homepage,name='homepage'),
    path('createcamp', views.createcamp,name='createcamp'),
    path('activecamp', views.activecamp,name='activecamp'),
    path('viewuser', views.viewuser,name='viewuser'),
    path('report', views.report,name='report'),
    path('userhomepage', views.userhomepage,name='userhomepage'),
    path('userdonate', views.userdonate,name='userdonate'),
    path('userdonate/<int:id>', views.userdonate,name='userdonate'),
    path('viewuserdonation', views.viewuserdonation,name='viewuserdonation'),
    path('register', views.register,name='register'),
    path('userviewcamp', views.userviewcamp,name='userviewcamp'),
]
