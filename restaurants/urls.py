from django.urls import re_path

from restaurants import views

urlpatterns = [
    re_path(r'^inspector_all_restaurants/', views.inspector_all_restaurants),
    re_path(r'^user_all_restaurants/', views.user_all_restaurants),
    re_path(r'^restaurant_home/', views.restaurant_home),
    re_path(r'^restaurant_details/(?P<idd>\w+)', views.restaurant_details,name='restaurant_details'),
]