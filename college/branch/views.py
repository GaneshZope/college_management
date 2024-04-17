from django.shortcuts import render
from django.http import JsonResponse
from .models import Branch

def branch(request):
    if request.method == 'GET':
        branchs=Branch.objects.all()
        branch_data = []
        for branch in branchs:
            branch_data.append({
                "branch_name":branch.name,
                "branch_description":branch.description


            })
        return JsonResponse(branch_data,safe=False)


