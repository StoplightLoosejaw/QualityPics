"""qualitypics URL Configuration

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
from api import views

urlpatterns = [
    path('accounts/logout/', views.user_logout, name='logout'),
    path('accounts/login/', views.user_login, name='login'),
    path('adm', views.PicListView.as_view(), name=None),
    path('', views.Home, name='QUALITY PICS'),
    path('id/<int:pk>', views.SinglePicView.as_view(), name=None),
    path('randompic', views.RandomPicView.as_view(), name=None),


]
