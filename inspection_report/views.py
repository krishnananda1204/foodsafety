from django.shortcuts import render
from django.http import HttpResponseRedirect
from inspection_report.models import InspectionReport
import datetime
from django.core.files.storage import FileSystemStorage


# Create your views here.


def add_inspection_report(request,idd):
    uid = request.session["uid"]
    if request.method == "POST":
        obj = InspectionReport()

        report = request.FILES['report']
        fs = FileSystemStorage()
        filename = fs.save(report.name, report)
        obj.report = report.name

        obj.inspector_id =uid
        obj.restaurant_id = idd
        obj.date = datetime.date.today()
        obj.time = datetime.datetime.now().strftime("%I:%M:%S")
        obj.save()
        alert = {
            'msg': "Successfully added !!!"
        }
        return render(request, 'inspection_report/add_inspection_report.html',alert)
    return render(request,'inspection_report/add_inspection_report.html')


