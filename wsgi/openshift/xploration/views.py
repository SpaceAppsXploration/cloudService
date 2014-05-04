'''
Homepage and REST views
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
from rest_framework.decorators import api_view

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
@api_view(['GET'])
def targets_list(request):
    '''
    List all possible Targets.
    These are different kinds of celestial bodies in the Solar system,
    that can be the mission's destination.
    '''
    if request.method == 'GET':
        targets = Targets.objects.all()
        serializer = TargetsSerializer(targets, many=True)
        return JSONResponse(serializer.data)
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint', 'type': 'null', 'content': 'null'}
        return JSONResponse(mex)

@csrf_exempt
@api_view(['GET'])
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
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint', 'type': 'null', 'content': 'null'}
        return JSONResponse(mex)

@csrf_exempt
@api_view(['GET'])
def missions_list(request):
    '''
    List all possible Missions.
    Use this call as few as possible, store the object in a local object,
    and refresh it seldomly. Use the stored object for daily tasks in the app.
    '''
    if request.method == 'GET':
        mix = Missions.objects.all()
        serializer = MissionsSerializer(mix, many=True)
        return JSONResponse(serializer.data)
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint', 'type': 'null', 'content': 'null'}
        return JSONResponse(mex)

@csrf_exempt
@api_view(['GET'])
def planets_list(request):
    '''
    List of all Planets physical values.
    'target' is the planet's id into Targets.
    '''
    if request.method == 'GET':
        mix = Planets.objects.all()
        serializer = PlanetsSerializer(mix, many=True)
        return JSONResponse(serializer.data)
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint', 'type': 'null', 'content': 'null'}
        return JSONResponse(mex)

@csrf_exempt
@api_view(['GET'])
def single_planet(request, p_id):
    '''
    Get  single Planets physical values
    'target' is the planet's id into Targets.
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
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint', 'type': 'null', 'content': 'null'}
        return JSONResponse(mex)

@csrf_exempt
@api_view(['GET'])
def single_mission(request, m_id):
    '''
    Get single mission by mission id.
    'targets' is an array of destinations' ids.
    Era = (1, Past), (2, Present), (3, Future), (0, Concept)
    '''
    if request.method == 'GET':
        one_mission = Missions.objects.all().filter(id=m_id).first()
        if not one_mission:
            res = json.dumps({'code':1, 'status':'Error', 'message': 'No mission with this id', 'type': 'null', 'content': 'null'})
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
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint', 'type': 'null', 'content': 'null'}
        return JSONResponse(mex)


@csrf_exempt
@api_view(['GET'])
def mission_detail(request, m_id):
    '''
    Reply with all the data referred to one Missions.
    Search by mission id.
    Response is an array of objects with different 'type'.
    '''
    if request.method == 'GET':
        mix_details = Details.objects.all().filter(mission=m_id)
        if len(mix_details) == 0:
            res = json.dumps({'status': 'Error', 'code': 1, 'message': 'no mission with this id', 'type': 'null', 'content': 'null'})
            return StreamingHttpResponse(res, content_type="application/json")
        serializer = DetailsSerializer(mix_details)
        return JSONResponse(serializer.data)
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint', 'type': 'null', 'content': 'null'}
        return JSONResponse(mex)

@csrf_exempt
@api_view(['GET'])
def missions_by_target(request, t_id):
    '''
    Reply with all the data referred to one Targets.
    Search by target id.
    Era = (1, Past), (2, Present), (3, Future), (0, Concept)
    '''
    if request.method == 'GET':
        try:
            target = Targets.objects.get(id=t_id)
        except:
            res = json.dumps({'code':1, 'status':'Error', 'message': 'No destination with this id', 'type': 'null', 'content': 'null'})
            return StreamingHttpResponse(res, content_type="application/json")

        target_missions = Missions.objects.all().filter(target=target)
           
        serializer = MissionsSerializer(target_missions, many=True)
        return JSONResponse(serializer.data)
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint', 'type': 'null', 'content': 'null'}
        return JSONResponse(mex)


def home(request):
    js = {'status': 'Coming Soon...', 'response': 200, 'code': 0, 'type': 'null', 'content': 'null'}
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

    count=0
    
    return StreamingHttpResponse(json.dumps({'status': 'done', 'count': count }), content_type="application/json")


def homeTEST(request):
    js = {'status': 'Coming Soon...', 'response': 200, 'code': 0}
    js = json.dumps(js)
    
    params = {}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'
    params['status'] = js
    return render_to_response('home/homeTEST.html', params)

