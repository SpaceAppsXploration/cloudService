from django.shortcuts import render_to_response
import json

def start(request):
    
    params = {}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'
    params['status'] = js
    return render_to_response('home/destinations.html', params)
