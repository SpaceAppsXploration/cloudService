from django.shortcuts import render_to_response
import json
from chronos.models import Targets
from django.db.models import Q

from webapp.appdata.sim_missions import missions

def homeTEST(request):
    js = {'status': 'Coming Soon...', 'response': 200, 'code': 0}
    js = json.dumps(js)
    
    params = {}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'
    params['status'] = js
    return render_to_response('webapp/homeTEST.html', params)

def start(request):
    tg = Targets.objects.all().filter(use_in_sim=True)
    params = {'targets': tg}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'

    return render_to_response('webapp/01-destinations.html', params)

def mission(request, p_slug):
    dt = Targets.objects.all().filter(slug=p_slug)
    params = {'missions': missions}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'

    return render_to_response('webapp/02-mission.html', params)
