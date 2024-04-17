from django.shortcuts import render
from department.models import Department
from django.http import JsonResponse

def departmentapi(request):
    if request.method=='GET':
        data=[]
        department=Department.objects.all()
        for dept in department:
            data.append({'college':dept.college.name,'code':dept.code,'name':dept.name,'building_no':dept.building_no})
        return JsonResponse(data,safe=False)
    
