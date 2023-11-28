from django.shortcuts import render

import inspector_queries
from black_list.models import BlackList
import datetime
from public_user.models import PublicUser
from restaurants.models import Restaurants
from login.models import Login
from django.http import HttpResponseRedirect

# Create your views here.


def add_to_blacklist(request,idd):
    uid = request.session["uid"]
    if request.method == "POST":
        obj = BlackList()
        obj.restaurant_id=idd
        obj.inspector_id=uid
        obj.details = request.POST.get('add')
        obj.date = datetime.date.today()
        obj.save()

        obb = Restaurants.objects.get(restaurant_id=idd)
        obb.status = 'blacklisted'
        obb.save()

        log = Login.objects.get(user_id=idd,type='restaurant')
        log.type = 'blacklisted'
        log.save()
        return HttpResponseRedirect('/restaurants/inspector_all_restaurants/')
    return render(request,'black_list/add_to_blacklist.html')


def user_view_blacklist(request):
    uid = request.session["uid"]
    user_district = PublicUser.objects.get(user_id=uid)
    restaurants = Restaurants.objects.filter(district=user_district.district).values_list('restaurant_id')
    blacklist = BlackList.objects.filter(restaurant_id__in=restaurants)
    context = {
        'data': blacklist
    }
    return render(request,'black_list/user_view_blacklist.html',context)


def inspector_view_blacklist(request):
    uid = request.session["uid"]
    # user_district = PublicUser.objects.get(user_id=uid)

    blacklist = BlackList.objects.filter(inspector_id=uid).values_list('restaurant_id')
    print(blacklist)
    restaurants = Restaurants.objects.filter(restaurant_id__in=blacklist,status='blacklisted')
    context = {
        'data': restaurants
    }
    return render(request,'black_list/inspector_view_blacklist.html',context)


def remove_from_blacklist(request,idd):
    obj = BlackList.objects.get(restaurant_id=idd)
    obj.delete()

    obb = Restaurants.objects.get(restaurant_id=idd)
    obb.status = 'active'
    obb.save()

    occ = Login.objects.get(user_id=idd,type='blacklisted')
    occ.type = 'restaurant'
    occ.save()
    return HttpResponseRedirect('/black_list/inspector_view_blacklist/')

