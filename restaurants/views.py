from django.shortcuts import render
from restaurants.models import Restaurants
from login.models import Login
from public_user.models import PublicUser
from inspection_report.models import InspectionReport
from rating.models import Rating
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect

# Create your views here.


def inspector_all_restaurants(request):
    obj = Login.objects.filter(type='restaurant').values_list('user_id', flat=True)
    res = Restaurants.objects.filter(restaurant_id__in=obj,status='active')
    context = {
        'data': res
    }
    return render(request,'restaurants/inspector_all_restaurants.html',context)


def user_all_restaurants(request):
    uid = request.session["uid"]
    user_district = PublicUser.objects.get(user_id=uid)
    res = Restaurants.objects.filter(district=user_district.district,status='active')
    context = {
        'data': res
    }

    if request.method == "POST" and "search" in request.POST:
        keyword = request.POST.get("keyword")
        result = Restaurants.objects.filter(name__icontains=keyword,district=user_district.district,status='active')
        search_result = {
            'result':result,
            'data': res
        }
        return render(request,'restaurants/user_all_restaurants.html',search_result)
    return render(request,'restaurants/user_all_restaurants.html',context)


def restaurant_details(request,idd):
    obj = Restaurants.objects.filter(restaurant_id=idd)
    # obb = MenuItems.objects.filter(restaurant_id=idd)
    context = {
        'data': obj,
        # 'items': obb
    }
    return render(request,'restaurants/restaurant_details.html',context)


def restaurant_home(request):
    uid = request.session["uid"]

    #inpection report
    obj = InspectionReport.objects.filter(restaurant_id=uid)

    #ratings
    rat = Rating.objects.filter(restaurant_id=uid)
    context = {
        'reports':obj,
        'rat':rat
    }
    # if request.method == "POST":
    #     obb = MenuItems()
    #     obb.restaurant_id = uid
    #     obb.item = request.POST.get('item')
    #     obb.description = request.POST.get('description')
    #     obb.price = request.POST.get('price')
    #
    #     image = request.FILES['image']
    #     fs = FileSystemStorage()
    #     filename = fs.save(image.name, image)
    #     obb.image = image.name
    #
    #     obb.save()
    #     return HttpResponseRedirect('/restaurants/restaurant_home/#menu')
    return render(request,'restaurants/restaurant_home.html',context)
