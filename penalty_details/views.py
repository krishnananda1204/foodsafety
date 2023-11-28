from django.shortcuts import render

from penalty_details.models import PenaltyDetails
import datetime

# Create your views here.


def add_penalty(request,idd):
    uid = request.session["uid"]
    if request.method == "POST":
        obj = PenaltyDetails()
        obj.restaurant_id=idd
        obj.inspector_id = uid
        obj.penalty_details = request.POST.get('penalty')
        obj.date = datetime.date.today()
        obj.time = datetime.datetime.now().strftime("%I:%M:%S")
        obj.save()
    return render(request,'penalty_details/add_penalty.html')
