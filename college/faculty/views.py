from django.shortcuts import render
from faculty.models import Faculty
from django.http import JsonResponse

def faultyapi(request):
    if request.method=='GET':
        data=[]
        faculty=Faculty.objects.all()
        for facultys in faculty:
            data.append({"name":facultys.name,"department":facultys.department.name,"email_id":facultys.email_id,
                         "address":facultys.address})
        return JsonResponse(data,safe=False)
            
            
                
    
