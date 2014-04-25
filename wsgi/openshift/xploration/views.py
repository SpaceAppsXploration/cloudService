'''
Homepage, Simulator and REST views
'''
import json
from django.http import HttpResponse, StreamingHttpResponse
#import random
from django.shortcuts import render_to_response
from django.http import Http404
import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

'''
import verity tables for mission's checking
'''
from data.tables_Bodies import destinations
from data.tables_Missions import mission_type
from data.tables_BusVsMission import bus_vs_mission_type
from data.tables_BusVsDist import bus_vs_dist
from data.tables_BusVsBus import bus_vs_bus
from data.missions import missions
from data.missions_details import missions_details

'''
import models and json serializers
'''
from models import Missions, Targets, Details
from serializers import TargetsSerializer, MissionsSerializer, DetailsSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def targets_list(request):
    '''
    List all possible Targets
    '''
    if request.method == 'GET':
        targets = Targets.objects.all()
        serializer = TargetsSerializer(targets, many=True)
        return JSONResponse(serializer.data)
    else:
        mex = {'response': '404', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint'}
        return JSONResponse(mex)

@csrf_exempt
def target_detail(request, t_id):
    '''
    Reply with only one among Targets
    '''
    try:
        target = Targets.objects.get(id=t_id)
    except Targets.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TargetsSerializer(target)
        return JSONResponse(serializer.data)
    else:
        mex = {'response': '404', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint'}
        return JSONResponse(mex)

@csrf_exempt
def missions_list(request):
    '''
    List all possible Missions
    '''
    if request.method == 'GET':
        mix = Missions.objects.all()
        serializer = MissionsSerializer(mix, many=True)
        return JSONResponse(serializer.data)
    else:
        mex = {'response': '404', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint'}
        return JSONResponse(mex)

@csrf_exempt
def single_mission(request, m_id):
    '''
    List all possible Missions
    '''
    if request.method == 'GET':
        one_mission = Missions.objects.all().filter(id=m_id)[0]
        name_mission = one_mission.name
        all_target = Missions.objects.all().filter(name=name_mission)
        serializer = MissionsSerializer(all_target, many=True)
        return JSONResponse(serializer.data)
    else:
        mex = {'response': '404', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint'}
        return JSONResponse(mex)


@csrf_exempt
def mission_detail(request, m_id):
    '''
    Reply with all the data referred to one Missions.
    Search by mission id
    '''
    try:
        mix_details = Details.objects.all().filter(mission=m_id)
    except Targets.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DetailsSerializer(mix_details)
        return JSONResponse(serializer.data)
    else:
        mex = {'response': '404', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint'}
        return JSONResponse(mex)

@csrf_exempt
def missions_by_target(request, t_id):
    '''
    Reply with all the data referred to one Missions.
    Search by mission id
    '''
    try:
        target_missions = Missions.objects.all().filter(target=t_id)
        #mix_details = Details.objects.all().filter(mission=m_id)
    except Targets.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MissionsSerializer(target_missions)
        return JSONResponse(serializer.data)
    else:
        mex = {'response': '404', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint'}
        return JSONResponse(mex)


def home(request):
    js = {'status': 'Coming Soon...', 'response': 200, 'code': 0}
    js = json.dumps(js)
    
    params = {}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'
    params['status'] = js
    return render_to_response('home/home.html', params)

def test(request):
    js = {'code': 0, 'status': 'OK', 'response': 200}
    js = json.dumps(js)

    return StreamingHttpResponse(js, content_type="application/json")

def clean(request):
    '''
    # Script creazione record in Targets (9)
    for m in missions:
        tot_target = m['pageURL']
        inizio = tot_target.find('Target=')
        fine = tot_target.find('&Era=')
        target = tot_target[inizio+7:fine]
        if not Targets.objects.all().filter(name=target):
            newObj = Targets(name=target, body_type=1, image_url='Empty') # per ora setto tutti i tipi a 1 e le immagini a 'Empty'
            newObj.save()   
   
    # Script creazione record in Missions (ca. 252)
    for obj in missions:
        tot_target = obj['pageURL']
        inizio = tot_target.find('Target=')
        fine = tot_target.find('&Era=')
        target = tot_target[inizio+7:fine]
        
        destination = Targets.objects.all().filter(name=target)[0]

        era = tot_target[fine+5:]
        if era == 'Past':
            era = 1
        if era == 'Present':
            era = 2
        if era == 'Future':
            era = 3
        if era == 'Concept':
            era = 0

               
        tot_link = obj['link']
        name = obj['name']
        inizio = tot_link.find('&MCode=')
        hashed = tot_link[inizio+7:]
        newObj = Missions(target=destination, era=era, name=name, codename=name, hashed=hashed, image_url=obj['image'])
        newObj.save()
    
    # Script creazione record in Details (ca. 1200)
    for m in missions_details:
        name = m['name']
        data = m['data']
        mission_to_save = Missions.objects.all().filter(name=name)[0]
        for d in data:
            if 'image_link' in d:
                # type Fact
                to_save = Details(mission=mission_to_save, detail_type=d['type'], header=d['header'],
                    body=d['body'], image_link=d['image_link'])
                to_save.save()
            if 'date' in d:
                # type event (news, headlines, key_dates)
                to_save = Details(mission=mission_to_save, detail_type=d['type'], header=d['header'],
                    body=d['body'], date=datetime.datetime.strptime(d['date'], '%d %b %Y').date())
                to_save.save()
            else:
                #type Goals, accomp
                to_save = Details(mission=mission_to_save, detail_type=d['type'], header=d['header'],
                    body=d['body'])
                to_save.save()
    
    '''
    return StreamingHttpResponse(json.dumps({'status': 'done'}), content_type="application/json")


def homeTEST(request):
    js = {'status': 'Coming Soon...', 'response': 200, 'code': 0}
    js = json.dumps(js)
    
    params = {}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'
    params['status'] = js
    return render_to_response('home/homeTEST.html', params)

def simulation(request):

    ''' 
    GET example: 
    /simulation/?
        destination=mars
        &mission=prop_chem
        &opt_sensor=true
        &radio_sensor=false
        &spectrometer=true
        &probe=true
        &amplifierfier=false
    '''

    if 'destination' not in request.GET: # raise 404 if not destination in the URL
        raise Http404

    results = {}


    usr_planet = request.GET['destination']


    # cycles destinations in table_Bodies.py
    for p in destinations:
        if p['slug'] == usr_planet:
            usr_planet = p
    

    if 'mission' not in request.GET: # raise 404 if not mission in the URL
        raise Http404

    usr_mission_slug = request.GET['mission']
    #print  usr_planet['name'], usr_mission['name']

    # check compatibility planet/mission  
    if usr_planet[usr_mission_slug] != True :
        results = {'code': 1, 'Error': 'Error in mission type ' + usr_mission_slug }
        return StreamingHttpResponse(json.dumps(results), content_type="application/json")
        

    # take components from URL and dump into a list
    components = [k for k,v in request.GET.iteritems() if v == 'true']
    

    #components = ['opt_sensor', 'radio_sensor', 'spectrometer', 'probe', 'amplifier']
    #comp_samples = random.sample(components, random.randint(1, len(components)))

    # check components/mission compatibility - mission_type
    for e in components:
        #print e
        for k in mission_type:
            #print k
            if k['slug'] == usr_mission_slug:
                if k[e] != True: 
                    results = { 'code': 1, 'Error': 'Error in component ' + e }
                    return StreamingHttpResponse(json.dumps(results), content_type="application/json") 

    
    # get BUS components from URL
    busAll = {}
    for k,v in request.GET.iteritems():
        if v == 'bustrue':
            busAll[k] = True

    # check if systems and subsystems are compatible with type of mission - bus_vs_mission_type
    if len(busAll) != 0:
      for e in bus_vs_mission_type:
        if e['slug'] == usr_mission_slug:
            for k,v in busAll.iteritems():
                if e[k] != v:
                    results = {'code': 1, 'Error': 'Error in BUS in system ' + k }
                    return StreamingHttpResponse(json.dumps(results), content_type="application/json")

    

    usr_distance = usr_planet['distance']

    # check if destination's distance is compatible - bus_vs_dist
    if len(busAll) != 0:
        for e in bus_vs_dist:
            j = e['range_min']
            # return StreamingHttpResponse(json.dumps(j), content_type="application/json")
            if isinstance(j, str):
              if j < int(usr_distance):
                for k,v in busAll.iteritems():
                    if e[k] != v:
                        results = { 'code':1, 'Error': 'Error in BUS vs distance ' + k }
                        return StreamingHttpResponse(json.dumps(results), content_type="application/json")


    
    # check if the payload is compatible - bus_vs_bus
    if len(busAll) != 0:
      for e in bus_vs_bus:
        if e['slug'] == usr_mission_slug:
            for k,v in busAll.iteritems():
                if e[k] != v:
                    results = { 'code':1, 'Error': 'Error in BUS in payload check ' + k }
                    return StreamingHttpResponse(json.dumps(results), content_type="application/json")

    results = { 'code':0, 'status':'OK', 'message': 'Mission is way to go!' }
    return StreamingHttpResponse(json.dumps(results), content_type="application/json") 

        



