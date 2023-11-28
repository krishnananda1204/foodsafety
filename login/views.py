from django.shortcuts import render
from django.http import HttpResponseRedirect
from login.models import Login
from inspector_queries.models import InspectorQueries
from food_inspector.models import FoodInspector
from inspection_report.models import InspectionReport
# Create your views here.


def login(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        passw = request.POST.get("password")
        obj = Login.objects.filter(username=uname, password=passw)
        tp = ""
        for ob in obj:
            tp = ob.type
            uid = ob.user_id
            if tp == "admin":
                request.session["uid"] = uid
                return HttpResponseRedirect('/login/department_home/')
            elif tp == 'food inspector':
                request.session["uid"] = uid
                return HttpResponseRedirect('/food_inspector/inspector_home/')
            elif tp == 'user':
                request.session["uid"] = uid
                return HttpResponseRedirect('/public_user/user_home/')
            elif tp == 'restaurant':
                request.session["uid"] = uid
                return HttpResponseRedirect('/restaurants/restaurant_home/')
                # return render(request, 'temp/admin_homepage.html')
        objlist = "Username or Password incorrect... Please try again...!"
        context = {
            'msg': objlist,
        }
        return render(request, 'login/login.html', context)
    return render(request,'login/login.html')


def department_home(request):
    # all food inspectors
    obj = FoodInspector.objects.all()

    # queries
    obb = InspectorQueries.objects.filter(reply='pending')

    # report
    rep = InspectionReport.objects.all()
    print(rep)
    context = {
        'data':obj,
        'queries':obb,
        'report':rep
    }
    return render(request,'login/department_home.html',context)

