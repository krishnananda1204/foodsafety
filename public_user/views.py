from django.shortcuts import render
from public_user.models import PublicUser
from food_inspector.models import FoodInspector
from login.models import Login
from inspection_report.models import InspectionReport
from restaurants.models import Restaurants
from public_complaints.models import PublicComplaints
import datetime
from django.http import HttpResponseRedirect
from django.db.models import Q
from rating.models import Rating


def user_registration(request):
    if request.method == "POST":
        em = request.POST.get('email')
        ph = request.POST.get('phone')
        ds = request.POST.get("district")
        inspector_exist = FoodInspector.objects.filter(district=ds)
        if not inspector_exist:
            alert = {
                'msg': "Sorry !!! Food inspector is not available for your selected district!!!"
            }
            return render(request, 'public_user/user_registration.html', alert)
        already = PublicUser.objects.filter(Q(phone=ph) | Q(email=em)).exists()
        if already == False:
            obj = PublicUser()
            obj.name = request.POST.get("name")
            obj.district = request.POST.get("district")
            obj.phone = request.POST.get("phone")
            obj.email = request.POST.get("email")
            obj.save()

            obb = Login()
            obb.username = request.POST.get("email")
            obb.password = request.POST.get("password")
            obb.type = "user"
            obb.user_id = obj.user_id
            obb.save()
            alert = {
                'msg': "Registered successfully !!!"
            }
            return render(request, 'public_user/user_registration.html', alert)
        else:
            alert = {
                'msg': "Email Id/Phone number is already exist"
            }
            return render(request, 'public_user/user_registration.html', alert)
    return render(request, 'public_user/user_registration.html')


def user_home(request):
    uid = request.session["uid"]
    user_district = PublicUser.objects.get(user_id=uid)
    restaurants = Restaurants.objects.filter(district=user_district.district,status='active')[:3]

    #inspector
    user_inspector = FoodInspector.objects.get(district=user_district.district)

    #inspection report
    res = Restaurants.objects.filter(district=user_district.district).values_list('restaurant_id')
    reports = InspectionReport.objects.filter(restaurant_id__in=res)
    context = {
        'data': restaurants,
        'report': reports
    }
    if request.method == "POST":
        obj = PublicComplaints()
        obj.user_id = uid
        obj.complaint = request.POST.get("complaint")
        obj.date = datetime.date.today()
        obj.time = datetime.datetime.now().strftime("%I:%M:%S")
        obj.inspector_id = user_inspector.inspector_id
        obj.reply = "pending"
        obj.save()
        alert = {
            'msg': "Successfully posted !!!"
        }
        return render(request, 'public_user/user_home.html', alert)
    return render(request,'public_user/user_home.html',context)
