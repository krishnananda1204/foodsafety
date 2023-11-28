from django.urls import re_path

from inspector_queries import views

urlpatterns = [
    re_path(r'^reply_to_inspector_query/(?P<idd>\w+)', views.reply_to_inspector_query,name='reply_to_inspector_query'),
    re_path(r'^inspector_view_query_reply/', views.inspector_view_query_reply,name='inspector_view_query_reply'),
]