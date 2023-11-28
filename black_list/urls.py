from django.urls import re_path

from black_list import views

urlpatterns = [
    re_path(r'^add_to_blacklist/(?P<idd>\w+)', views.add_to_blacklist,name='add_to_blacklist'),
    re_path(r'^remove_from_blacklist/(?P<idd>\w+)', views.remove_from_blacklist,name='remove_from_blacklist'),
    re_path(r'^user_view_blacklist/', views.user_view_blacklist,name='user_view_blacklist'),
    re_path(r'^inspector_view_blacklist/', views.inspector_view_blacklist,name='inspector_view_blacklist')
]