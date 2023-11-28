from django.urls import re_path

from rating import views

urlpatterns = [
    re_path(r'^add_rating/(?P<idd>\w+)', views.add_rating,name='add_rating'),

]