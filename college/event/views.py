from django.shortcuts import render
from django.http import JsonResponse
from .models import Event

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






