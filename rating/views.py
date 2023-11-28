from django.shortcuts import render
from rating.models import Rating
import datetime
# Create your views here.


def add_rating(request,idd):
    uid = request.session["uid"]
    if request.method == "POST":
        rating = request.POST.get("stars")
        comment = request.POST.get("comment")
        obj = Rating()
        obj.user_id = uid
        obj.restaurant_id = idd
        obj.rating = rating
        obj.comment = comment
        obj.date = datetime.date.today()
        obj.time = datetime.datetime.now().strftime("%I:%M:%S")
        obj.save()
        alert = {
            'msg': "Successfully added !!!"
        }
        return render(request, 'rating/add_rating.html',alert)
    return render(request,'rating/add_rating.html')
