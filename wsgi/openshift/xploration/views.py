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
#from data.missions import missions
#from data.missions_details import missions_details


'''
import models and json serializers
'''
from models import Missions, Targets, Details, Planets
from serializers import TargetsSerializer, MissionsSerializer, DetailsSerializer, PlanetsSerializer


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
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint'}
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
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint'}
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
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint'}
        return JSONResponse(mex)

@csrf_exempt
def planets_list(request):
    '''
    List of all Planets physical values
    '''
    if request.method == 'GET':
        mix = Planets.objects.all()
        serializer = PlanetsSerializer(mix, many=True)
        return JSONResponse(serializer.data)
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint'}
        return JSONResponse(mex)

@csrf_exempt
def single_planet(request, p_id):
    '''
    Get  single Planets physical values
    '''
    if request.method == 'GET':
        mix = Planets.objects.get(target=p_id)
        name = Targets.objects.get(id=p_id).name
        obj = {'target': mix.target.id, 'name': name, 'discover': mix.discover,
            'rings': mix.rings, 'light': mix.light, 'mass': mix.mass, 'diameter': mix.diameter,
            'density': mix.density, 'gravity': mix.gravity, 'l_day': mix.l_day, 'l_year': mix.l_year,
            'eccent': mix.eccent, 'distance': mix.distance, 'perihelion': mix.perihelion, 
            'aphelion': mix.aphelion, 'inclination': mix.inclination, 'atmosphere': mix.atmosphere }
        serializer = json.dumps(obj)
        return StreamingHttpResponse(serializer, content_type="application/json")
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint'}
        return JSONResponse(mex)

@csrf_exempt
def single_mission(request, m_id):
    '''
    Get single mission by mission id
    '''
    if request.method == 'GET':
        one_mission = Missions.objects.all().filter(id=m_id).first()
        if not one_mission:
            res = json.dumps({'code':1, 'status':'Error', 'message': 'No mission with this id'})
            return StreamingHttpResponse(res, content_type="application/json") 
        name_mission = one_mission.name
        all_target = Missions.objects.all().filter(name=name_mission)
        mission_targets = []
        for t in all_target:
            mission_targets.append(t.target.id)
        obj = {'target': mission_targets, 'era': one_mission.era, 'name': one_mission.name,
               'codename': one_mission.codename, 'hashed': one_mission.hashed, 'image_url': one_mission.image_url,
               'launch_dates': one_mission.launch_dates  }
        serializer = json.dumps(obj)
        return StreamingHttpResponse(serializer, content_type="application/json")
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint'}
        return JSONResponse(mex)


@csrf_exempt
def mission_detail(request, m_id):
    '''
    Reply with all the data referred to one Missions.
    Search by mission id
    '''
    if request.method == 'GET':
        mix_details = Details.objects.all().filter(mission=m_id)
        if len(mix_details) == 0:
            res = json.dumps({'status': 'Error', 'code': 1, 'message': 'no mission with this id'})
            return StreamingHttpResponse(res, content_type="application/json")
        serializer = DetailsSerializer(mix_details)
        return JSONResponse(serializer.data)
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint'}
        return JSONResponse(mex)

@csrf_exempt
def missions_by_target(request, t_id):
    '''
    Reply with all the data referred to one Targets.
    Search by target id
    '''
    if request.method == 'GET':
        try:
            target = Targets.objects.get(id=t_id)
        except:
            res = json.dumps({'code':1, 'status':'Error', 'message': 'No destination with this id'})
            return StreamingHttpResponse(res, content_type="application/json")

        target_missions = Missions.objects.all().filter(target=target)
           
        serializer = MissionsSerializer(target_missions)
        return JSONResponse(serializer.data)
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint'}
        return JSONResponse(mex)


def home(request):
    js = {'status': 'Coming Soon...', 'response': 200, 'code': 0}
    js = json.dumps(js)
    
    params = {}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'
    params['status'] = js
    return render_to_response('home/home.html', params)

def test(request):
    #from data.ESA_output_COMPLETE import missions
    count = 0 
    
    return StreamingHttpResponse(json.dumps({'status': 'finished', 'count': count}), content_type="application/json")

def clean(request):

    count = 0
    
    return StreamingHttpResponse(json.dumps({'status': 'done', 'count': count }), content_type="application/json")


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
        results = {'code': 1, 'status': 'Error', 'message':'Error in simulation', 
                   'type': 'Error in mission type ' + usr_mission_slug, 'content': 'null' }
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
                    results = { 'code': 1, 'status': 'Error', 'message':'Error in simulation', 
                                'type': 'Error in component ' + e, 'content': 'null' }
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
                    results = {'code': 1, 'status': 'Error', 'message':'Error in simulation', 
                               'type': 'Error in BUS in system ' + k, 'content': 'null' }
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
                        results = { 'code':1, 'status': 'Error', 'message':'Error in simulation', 
                                    'type': 'Error in BUS vs distance check ' + k, 'content': 'null' }
                        return StreamingHttpResponse(json.dumps(results), content_type="application/json")


    
    # check if the payload is compatible - bus_vs_bus
    if len(busAll) != 0:
      for e in bus_vs_bus:
        if e['slug'] == usr_mission_slug:
            for k,v in busAll.iteritems():
                if e[k] != v:
                    results = { 'message':'Error in simulation', 'type': 'Error in BUS vs payload check ' + k,
                               'content': 'null', 'code':1, 'status': 'Error' }
                    return StreamingHttpResponse(json.dumps(results), content_type="application/json")

    results = { 'code':0, 'status':'OK', 'message': 'Mission is way to go!', 'type': 'cheer', 'content': 'null' }
    return StreamingHttpResponse(json.dumps(results), content_type="application/json") 

        



