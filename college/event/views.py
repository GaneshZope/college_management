from django.shortcuts import render
from django.http import JsonResponse
from .models import Event
import json

def event(request):
    if request.method == 'GET':
        events=Event.objects.all()
        event_data = []
        for event in events:
            event_data.append({
                "event_name":event.name,
                "event_description":event.description


            })
        return JsonResponse(event_data,safe=False)
    
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description')
        
        event= Event.objects.create(
            name = name ,
            description = description
            
        )
        return JsonResponse({'message': 'Event Data Created Succesfull' })
    
    
    if request.method == 'PUT':
        data = json.loads(request.body)
        event_id = data.get('event_id')
        try:
            event = Event.objects.get(id=event_id)
            event.name = data.get('name', event.name)
            event.description = data.get('description', event.description)
            event.save()
            return JsonResponse({
                'message': 'Event Data Update Succesfull'
            })
        
        except Event.DoesNotExist:
            return JsonResponse({
                'message': 'Event ID Does Not Exist'
             })






# elif request.method == 'PUT':
#         data = json.loads(request.body)
#         company_id = data.get('company_id')
#         try:
#             company = Company.objects.get(id=company_id)
#             company.name = data.get('name', company.name)
#             company.logo = data.get('logo', company.logo)
#             company.save()
#             return prepare_response(
#                 message=constants.DATA_UPDATE_SUCCESSFUL,
#                 status=status.HTTP_200_OK
#             )
#         except Company.DoesNotExist:
#             return prepare_response(
#                 message=constants.INVALID_INPUTS,
#                 status=status.HTTP_400_BAD_REQUEST

