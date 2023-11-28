from django.shortcuts import render
from public_complaints.models import PublicComplaints
from django.http import HttpResponseRedirect

# Create your views here.


def reply_to_public_complaint(request,idd):
    obb = PublicComplaints.objects.filter(complaint_id=idd)
    context = {
        'data':obb
    }
    if request.method == "POST":
        obj = PublicComplaints.objects.get(complaint_id=idd)
        obj.reply =request.POST.get('reply')
        obj.save()
        alert = {
            'msg': "Successfully added !!!"
        }
        return render(request, 'public_complaints/reply_to_public_complaint.html', alert)
    return render(request, 'public_complaints/reply_to_public_complaint.html',context)


def user_view_reply(request):
    uid = request.session["uid"]
    obj = PublicComplaints.objects.filter(user_id=uid)
    context = {
        'complaints': obj
    }
    return render(request,'public_complaints/user_view_complaint_reply.html',context)
