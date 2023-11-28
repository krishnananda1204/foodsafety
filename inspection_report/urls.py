from django.urls import re_path

from inspection_report import views

urlpatterns = [
    re_path(r'^add_inspection_report/(?P<idd>\w+)', views.add_inspection_report,name='add_inspection_report'),
]