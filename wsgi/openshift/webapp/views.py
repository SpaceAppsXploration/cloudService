from django.shortcuts import render_to_response
import json
from chronos.models import Targets, PayloadBusComps
#from django.db.models import Q
from django.core.cache import cache

from webapp.appdata.sim_missions import missions

def homeTEST(request):
    js = {'status': 'Coming Soon...', 'response': 200, 'code': 0}
    js = json.dumps(js)
    
    params = {}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'
    params['status'] = js
    return render_to_response('webapp/homeTEST.html', params)

def start(request):
    if cache.get('destinations') is not None:
        tg = cache.get('destinations')
        print 'found'
    else:
        tg = Targets.objects.all().filter(use_in_sim=True).order_by('name')
        cache.set('destinations', tg, 7200)
        print 'not found'

    params = {'targets': tg}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'

    return render_to_response('webapp/01-destinations.html', params)

def mission(request, p_slug):
    dt = Targets.objects.get(slug=p_slug)
    params = {'missions': missions, 'destination': p_slug, 'd_obj': dt}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'

    return render_to_response('webapp/02-mission.html', params)

def payload(request, p_slug, m_slug):
    dt = Targets.objects.get(slug=p_slug)
    pl = PayloadBusComps.objects.all().filter(category='payload')
    for m in missions:
        for k,v in m.iteritems():
            if v == m_slug:
                ms = m
                break
    params = {'missions': missions, 'payloads': pl, 'destination': p_slug, 'd_obj': dt,
               'm_obj': ms}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'

    return render_to_response('webapp/03-payload.html', params)

def bus(request, p_slug, m_slug, pl_slug):
    dt = Targets.objects.get(slug=p_slug)
    pl = PayloadBusComps.objects.all().filter(category='payload')
    bus = PayloadBusComps.objects.all().filter(category='bus').order_by('pbtype__name')
    for m in missions:
        for k,v in m.iteritems():
            if v == m_slug:
                ms = m
                break
    pl_slugs = pl_slug.split('-')
    
    pl_assembled = set()
    assembled_slugs = '&'
    for p in pl:
        for l in pl_slugs:
            if p.slug == l:
                pl_assembled.add(p)
                assembled_slugs = assembled_slugs+p.slug+'=true&'
    print pl_assembled
    params = {'missions': missions, 'payloads': pl, 'destination': p_slug, 'd_obj': dt,
               'm_obj': ms, 'assembled': pl_assembled, 'assembled_slugs': assembled_slugs, 'bus': bus}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'

    return render_to_response('webapp/04-bus.html', params)

def results(request, p_slug, m_slug, pl_slug, bus_slug):
    dt = Targets.objects.get(slug=p_slug)
    pl = PayloadBusComps.objects.all().filter(category='payload')
    bus = PayloadBusComps.objects.all().filter(category='bus')
    for m in missions:
        for k,v in m.iteritems():
            if v == m_slug:
                ms = m
                break
    pl_slugs = pl_slug.split('-')
    
    pl_assembled = set()
    assembled_slugs = '&'
    for p in pl:
        for l in pl_slugs:
            if p.slug == l:
                pl_assembled.add(p)
                assembled_slugs = assembled_slugs+p.slug+'=true&'
    print pl_assembled

    bus_assembled = set()
    bus_slugs = bus_slug.split('-')
    for b in bus:
        for s in bus_slugs:
            if b.slug == s:
                 bus_assembled.add(b)
    print bus_assembled

    params = {'missions': missions, 'payloads': pl, 'destination': p_slug, 'd_obj': dt,
               'm_obj': ms, 'assembled': pl_assembled, 'assembled_slugs': assembled_slugs, 'bus': bus,
                'bus_assembled': bus_assembled}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'

    return render_to_response('webapp/05-results.html', params)