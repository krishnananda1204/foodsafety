from django.urls import re_path

from penalty_details import views

urlpatterns = [
    re_path(r'^add_penalty/(?P<idd>\w+)', views.add_penalty,name='add_penalty'),
]