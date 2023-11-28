from django.urls import re_path
from food_inspector import views

urlpatterns = [
    re_path(r'^add_inspectors/', views.add_inspectors),
    re_path(r'^inspector_home/', views.inspector_home),
   re_path(r'^update_food_inspector/(?P<idd>\w+)', views.update_food_inspector,name='update_food_inspector'),
    re_path(r'^delete_food_inpector/(?P<idd>\w+)', views.delete_food_inpector,name='delete_food_inpector'),
]