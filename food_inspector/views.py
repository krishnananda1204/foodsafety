from django.shortcuts import render
from food_inspector.models import FoodInspector
from login.models import Login
from restaurants.models import Restaurants
from public_complaints.models import PublicComplaints
from inspector_queries.models import InspectorQueries
from django.http import HttpResponseRedirect
import datetime
from django.core.files.storage import FileSystemStorage
from django.db.models import Q

# Create your views here.


def add_inspectors(request):
    dt= request.POST.get('district')
    ob = FoodInspector.objects.filter(district=dt).all()
    if ob:
        objlist = "Already registered with this district...!!!"
        context = {
            'msg': objlist,
        }
        return render(request,'food_inspector/add_inspectors.html',context)
    if request.method=="POST":
        em = request.POST.get('email')
        ph = request.POST.get('phone')
        already = FoodInspector.objects.filter(Q(phone=ph)|Q(email=em)).exists()
        if already == False:
            obj = FoodInspector()
            obj.name = request.POST.get('name')
            obj.age = request.POST.get('age')
            obj.address = request.POST.get('address')
            obj.district = request.POST.get('district')
            obj.email = request.POST.get('email')
            obj.phone = request.POST.get('phone')
            obj.qualification = request.POST.get('qualification')
            obj.experience = request.POST.get('experience')

            photo = request.FILES['photo']
            fs = FileSystemStorage()
            filename = fs.save(photo.name, photo)
            obj.photo = photo.name

            identity_proof = request.FILES['proof']
            ff = FileSystemStorage()
            filename = ff.save(identity_proof.name, identity_proof)
            obj.identity_proof = identity_proof.name

            obj.save()

            obb = Login()
            obb.username = request.POST.get('email')
            obb.password = request.POST.get('password')
            obb.type = "food inspector"
            obb.user_id = obj.inspector_id
            obb.save()
            alert = {
                'msg': "Registered successfully !!!"
            }
            return render(request, 'food_inspector/add_inspectors.html', alert)
        else:
            alert = {
                'msg': "Email Id/Phone number is already exist"
            }
            return render(request, 'food_inspector/add_inspectors.html', alert)
    return render(request,'food_inspector/add_inspectors.html')


def inspector_home(request):
    uid = request.session["uid"]

    obj = Login.objects.filter(type='restaurant pending').values_list('user_id',flat=True)
    res = Restaurants.objects.filter(restaurant_id__in=obj)

    # public complaints
    obb = PublicComplaints.objects.filter(inspector_id=uid,reply='pending')

    #add restaurants

    context = {
        'data':res,
        'comp':obb
    }
    if request.method == "POST" and "restaurant" in request.POST:
        em = request.POST.get('email')
        ph = request.POST.get('phone')
        already = Restaurants.objects.filter(Q(phone=ph) | Q(email=em)).exists()
        if already == False:
            obb = Restaurants()
            obb.name = request.POST.get('name')
            obb.address = request.POST.get('address')
            obb.district = request.POST.get('district')
            obb.email = request.POST.get('email')
            obb.phone = request.POST.get('phone')
            obb.owner_name = request.POST.get('owner_name')
            obb.owner_address = request.POST.get('owner_address')
            obb.owner_contact = request.POST.get('owner_phone')
            obb.status = "active"


            photo = request.FILES['photo']
            fs = FileSystemStorage()
            filename = fs.save(photo.name, photo)
            obb.photo = photo.name


            identity_proof = request.FILES['proof']
            ff = FileSystemStorage()
            filename = ff.save(identity_proof.name, identity_proof)
            obb.proof = identity_proof.name

            obb.save()

            obc = Login()
            obc.username = request.POST.get('email')
            obc.password = request.POST.get('password')
            obc.type = "restaurant"
            obc.user_id = obb.restaurant_id
            obc.save()
            alert = {
                'msg': "Successfully registered !!!"
            }
            return render(request, 'food_inspector/inspector_home.html', alert)
        else:
            alert = {
                'msg': "Email Id/Phone number is already exist"
            }
            return render(request, 'food_inspector/inspector_home.html', alert)

    if request.method == "POST" and "query" in request.POST:
        que = InspectorQueries()
        que.query = request.POST.get('query')
        que.date = datetime.date.today()
        que.time = datetime.datetime.now().strftime("%I:%M:%S")
        que.inspector_id = uid
        que.reply = "pending"
        que.save()
        alert = {
            'msg': "Successfully posted !!!"
        }
        return render(request, 'food_inspector/inspector_home.html', alert)
    return render(request,'food_inspector/inspector_home.html',context)


def update_food_inspector(request,idd):
    obj = FoodInspector.objects.filter(inspector_id=idd)
    log = Login.objects.filter(user_id=idd,type='food inspector')
    context = {
        'data': obj,
        'pas':log
    }
    if request.method=="POST":
        obj=FoodInspector.objects.get(inspector_id=idd)
        obj.name=request.POST.get('name')
        obj.age=request.POST.get('age')
        obj.address=request.POST.get('address')
        obj.district=request.POST.get('district')
        obj.email=request.POST.get('email')
        obj.phone=request.POST.get('phone')
        obj.qualification=request.POST.get('qualification')
        obj.experience=request.POST.get('experience')

        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        obj.photo = photo.name

        identity_proof = request.FILES['proof']
        ff = FileSystemStorage()
        filename = ff.save(identity_proof.name, identity_proof)
        obj.identity_proof = identity_proof.name

        obj.save()

        obb=Login.objects.get(user_id=idd,type='food inspector')
        obb.username=request.POST.get('email')
        obb.password=request.POST.get('password')
        obb.save()
        return HttpResponseRedirect('/login/department_home/#menu')
    return render(request, 'food_inspector/update_food_inpector.html', context)


def delete_food_inpector(request,idd):
    obj = FoodInspector.objects.get(inspector_id=idd)
    obj.delete()

    obb = Login.objects.get(user_id=idd,type='food inspector')
    obb.delete()
    return HttpResponseRedirect('/login/department_home/#menu')



