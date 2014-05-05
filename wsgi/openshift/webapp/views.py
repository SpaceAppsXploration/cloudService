from django.shortcuts import render_to_response
import json
from chronos.models import Targets
from django.db.models import Q


def start(request):
    tg = Targets.objects.all().filter(~Q(name='Surface'))
    params = {'targets': tg}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'

    return render_to_response('home/destinations.html', params)
