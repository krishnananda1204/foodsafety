from django.urls import re_path

from public_user import views

urlpatterns = [
    re_path(r'^user_registration/', views.user_registration,name='user_registration'),
    re_path(r'^user_home/', views.user_home),
]