from django.shortcuts import render
from django.http import JsonResponse
from .models import Branch
import json

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


    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description')
        
        branch= Branch.objects.create(
            name = name ,
            description = description
            
        )
        return JsonResponse({'message': 'Branch Data Created Succesfull' })
    

    if request.method == 'PUT':
        data = json.loads(request.body)
        branch_id = data.get('branch_id')
        try:
            branch = Branch.objects.get(id=branch_id)
            branch.name = data.get('name', branch.name)
            branch.description = data.get('description', branch.description)
            branch.save()
            return JsonResponse({
                'message': 'Branch Data Update Succesfull'
            })
        
        except Branch.DoesNotExist:
            return JsonResponse({
                'message': 'Branch ID Does Not Exist'
             })


