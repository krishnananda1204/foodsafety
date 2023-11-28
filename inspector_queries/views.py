from django.shortcuts import render
from inspector_queries.models import InspectorQueries
from django.http import HttpResponseRedirect

# Create your views here.


def reply_to_inspector_query(request,idd):
    obj = InspectorQueries.objects.filter(i_query_id=idd)
    context = {
        'data':obj
    }
    if request.method=="POST":
        obj=InspectorQueries.objects.get(i_query_id=idd)
        obj.reply=request.POST.get('reply')
        obj.save()
        alert = {
            'msg': "Successfully posted !!!"
        }
        return render(request, 'inspector_queries/reply_to_inspector_query.html', alert)
    return render(request,'inspector_queries/reply_to_inspector_query.html',context)


def inspector_view_query_reply(request):
    uid = request.session["uid"]
    obj = InspectorQueries.objects.filter(inspector_id=uid)
    context = {
        'data': obj
    }
    return render(request, 'inspector_queries/inspector_view_query_reply.html',context)
