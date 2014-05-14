from django.shortcuts import render_to_response
import json
from chronos.models import Targets, PayloadBusComps, Missions, Details, Planets
#from django.db.models import Q
from django.core.cache import cache
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage

from webapp.appdata.sim_missions import missions
from data import ratings
from data import levels

def homeTEST(request):
    js = {'status': 'Coming Soon...', 'response': 200, 'code': 0}
    js = json.dumps(js)
    
    params = {}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'
    params['status'] = js
    return render_to_response('webapp/homeTEST.html', params)

def start(request):
    tg = Targets.objects.all().filter(use_in_sim=True).order_by('name')


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
    agencies = Missions.objects.all().filter(target=dt)
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
    

    bus_assembled = set()
    bus_slugs = bus_slug.split('-')
    for b in bus:
        for s in bus_slugs:
            if b.slug == s:
                 bus_assembled.add(b)
    #print bus_assembled
    
    # calculate ratings
    int_index = int(round(ratings[p_slug][0]*.6 + ratings[m_slug][0]*.4))
    
    pl_cost = 0
    for pl in pl_slugs:
        pl_cost += ratings[pl][1]

    pl_cost = pl_cost / len(pl_slugs)
    
    bus_cost = 0
    for bus in bus_slugs:
        bus_cost +=  ratings[bus][1]

    bus_cost = bus_cost / len(bus_slugs)

    cost_index = int(round(ratings[p_slug][1]*.5 + pl_cost*.2 + bus_cost*.3))

    risk_index = int(round(ratings[p_slug][2]*.5 + ratings[m_slug][2]*.5))
    
    print int_index, cost_index, risk_index
    
    interest = (int_index, levels['interest'][int_index])
    cost     = (cost_index, levels['cost'][cost_index])
    risk     = (risk_index, levels['risk'][risk_index])

    params = {'missions': missions, 'payloads': pl, 'destination': p_slug, 'd_obj': dt,
               'm_obj': ms, 'assembled': pl_assembled, 'assembled_slugs': assembled_slugs, 'bus': bus,
                'bus_assembled': bus_assembled, 'bus_slugs': bus_slugs, 'pl_slugs': pl_slugs}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'
    
    params['interest_level'] = interest
    params['cost_level']     = cost
    params['risk_level']     = risk
    params['agencies']       = agencies

    details = set()
    for a in agencies:
        d = Details.objects.all().filter(mission=a).first()
        details.add(d)

    params['details']       = details

    if request.GET.get('page') is not None:
        params['ref'] = request.GET.get('ref')

    return render_to_response('webapp/05-results.html', params)


def datavis(request, what):
    js = {'status': 'Coming Soon...', 'response': 200, 'code': 0}
    js = json.dumps(js)
    
    if what == 'planets':
       bodies = Planets.objects.all()

    elif what == 'missions':
        bodies = Missions.objects.all().order_by('name')
        paginator = Paginator(bodies, 10) # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            bodies = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            bodies = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            bodies = paginator.page(paginator.num_pages)

    elif what == 'components':
        bodies = PayloadBusComps.objects.all()
    else:
        raise Http404

    if request.GET.get('page') is None:
        page = 1
    params = {}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'
    params['status'] = js
    params['bodies'] = bodies
    params['what'] = what
    params['page'] = page
    return render_to_response('webapp/showdata.html', params)

def details_page(request, m_id):
    params = {}

    m = Missions.objects.all().get(id=m_id)
    name = m.name
    print name

    page = request.GET.get('page')

    Allm = Missions.objects.all().filter(name=name)
    Alld = set()
    for a in Allm:
        try:
            obj = Details.objects.all().filter(mission=a.id).first()
            try:
                mix_details = Details.objects.all().filter(mission=obj.mission.id)
                for o in mix_details:
                    Alld.add(o.id)
            except:
                pass
        except:
            pass
        
    details = Details.objects.filter(id__in=Alld)
    
    params['details'] = details
    params['back_page'] = page
    params['m_name'] = name
    
    if request.GET.get('page') is not None:
        params['ref'] = request.GET.get('ref')

    return render_to_response('webapp/details.html', params)

def instructions(request):
    params = {}

    return render_to_response('webapp/instructions.html', params)


from django.template import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def wphoneregister(request):

    from django.template import RequestContext
    from django.core.context_processors import csrf

    if request.method == 'GET':
        params = {}

        return render_to_response('webapp/wphonebeta.html', params,
                              context_instance=RequestContext(request))


    if request.method == 'POST':
        subscriber = request.POST['subscriber']

        to = "dev.xploration@outlook.com"
        sender = "Xploration Page <dev.xploration@outlook.com>"
        subject = "BETA ENROLLMENT REQUEST"
        content_txt = '''Somebody asked to enroll: \n
                       Email: '''+subscriber+'''\n
                       '''
        message = EmailMessage(subject, content_txt, from_email=sender, to=[to])
            
        message.send()

        msg = {'message': 'Thanks for enrolling, you will receive an email with further instructions from our developers soon.'}
        return render_to_response('users/register.html', msg,
                              context_instance=RequestContext(request))
