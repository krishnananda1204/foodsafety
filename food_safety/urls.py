"""food_safety URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.urls import re_path
from login import views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^black_list/',include('black_list.urls')),
    re_path(r'^food_inspector/',include('food_inspector.urls')),
    re_path(r'^inspection_report/',include('inspection_report.urls')),
    re_path(r'^inspector_queries/',include('inspector_queries.urls')),
    re_path(r'^login/',include('login.urls')),
    re_path(r'^penalty_details/',include('penalty_details.urls')),
    re_path(r'^public_complaints/',include('public_complaints.urls')),
    re_path(r'^public_user/',include('public_user.urls')),
    re_path(r'^restaurants/',include('restaurants.urls')),
    re_path(r'^rating/',include('rating.urls')),
    re_path('$',views.login),
]
