from django.urls import re_path

from public_complaints import views

urlpatterns = [
    re_path(r'^reply_to_public_complaint/(?P<idd>\w+)', views.reply_to_public_complaint,name='reply_to_public_complaint'),
   re_path(r'^user_view_reply/', views.user_view_reply,name='user_view_reply'),
]
