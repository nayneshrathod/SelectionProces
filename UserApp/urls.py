"""SelectionProc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from UserApp import views
from UserApp.views import *

urlpatterns = [
    path('', views.index, name="Index"),
    path('home/', views.home, name="home"),
    path('login/', views.Use_login, name="usr_login"),
    path('register/', views.register, name="usr_register"),
    path('logout/', views.uslogout, name="usr_logout"),
    path('addpost/', views.addpost, name="adingpost"),
    # path('success/', views.success, name="usr_success"),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
