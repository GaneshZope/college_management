from django.shortcuts import render
from collge.models import College
from django.http import JsonResponse



def collageapi(request):
    data=[]
    if request.method =='GET':
        college_data=College.objects.all()
        for collage in college_data:
            data.append({"code":collage.code,"name":collage.name,"address":collage.address})
        return JsonResponse(data,safe=False)
                            
