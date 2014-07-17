"""
REST views and Map Generator
Need refactoring
"""
import json
import re
from django.http import HttpResponse, StreamingHttpResponse
#import random
from django.shortcuts import render_to_response
from django.http import Http404
import datetime
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view


"""
import models and json serializers
"""
from models import Missions, Targets, Details, Planets, PayloadBusTypes, PayloadBusComps, SciData
from serializers import TargetsSerializer, MissionsSerializer, DetailsSerializer, PlanetsSerializer, PayloadBusCompsSerializer, PayloadBusTypesSerializer, SciDataSerializer


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
    """
    List all possible Targets.
    These are different kinds of celestial bodies in the Solar system,
    that can be the mission's destination.
    """
    if request.method == 'GET':
        targets = Targets.objects.all().order_by('id')
        serializer = TargetsSerializer(targets, many=True)
        return JSONResponse(serializer.data)
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint', 'type': 'null', 'content': 'null'}
        return JSONResponse(mex)

@csrf_exempt
@api_view(['GET'])
def target_detail(request, t_id):
    """
    Reply with only one among Targets
    """
    try:
        target = Targets.objects.get(id=t_id)
    except Targets.DoesNotExist:
        mex = {'status': 'Error', 'code': 1, 'message': 'No target with this id', 'type': 'null', 'content': 'null'}
        return JSONResponse(mex)

    if request.method == 'GET':
        serializer = TargetsSerializer(target)
        return JSONResponse(serializer.data)
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint', 'type': 'null', 'content': 'null'}
        return JSONResponse(mex)

@csrf_exempt
@api_view(['GET'])
def missions_list(request):
    """
    List all possible Missions.
    Use this call as few as possible, store the object in a local object,
    and refresh it seldomly. Use the stored object for daily tasks in the app.
    """
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
    """
    List of all Planets physical values.
    'target' is the planet's id into Targets.
    """
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
    """
    Get  single Planets physical values
    'target' is the planet's id into Targets.
    """
    if request.method == 'GET':
        try:
            mix = Planets.objects.get(target=p_id)
        except:
            mex = {'status': 'Error', 'code': 1, 'message': '404', 'type': 'null', 'content': 'null'}
            return JSONResponse(mex)
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
    """
    Get single mission by mission id.
    'targets' is an array of destinations' ids.
    Era = (1, Past), (2, Present), (3, Future), (0, Concept)
    """
    if request.method == 'GET':
        one_mission = Missions.objects.all().get(id=m_id)
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
    """
    Reply with all the data referred to one Missions.
    Search by mission id.
    Response is an array of objects with different 'detail_type'.
    """
    if request.method == 'GET':
        try:
            m = Missions.objects.get(id=m_id)
            cdn = m.codename
            #print cdn
        except:
            res = json.dumps({'status': 'Error', 'code': 1, 'message': 'no details for this mission', 'type': 'null', 'content': 'null'})
            return StreamingHttpResponse(res, content_type="application/json")
        
        # Missions are stored in the DB considering the (mission,target) coupling
        # (Missions with multiple Targets are stored in multiple records)
        # So it happens that Details are referred to only one of this couple
        # Need to cycle into all these couples, to find the ForeignKey used by
        # the Details referred to that mission
        Allm = Missions.objects.all().filter(codename=cdn)
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
        
        Alld = Details.objects.filter(id__in=Alld)
        serializer = DetailsSerializer(Alld, many=True)
        return JSONResponse(serializer.data)
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint', 'type': 'null', 'content': 'null'}
        return JSONResponse(mex)

@csrf_exempt
@api_view(['GET'])
def missions_by_target(request, t_id):
    """
    Reply with all the data referred to one Targets.
    Search by target id.
    Era = (1, Past), (2, Present), (3, Future), (0, Concept)
    """
    if request.method == 'GET':
        if t_id.isdigit():
            try:
                target = Targets.objects.get(id=t_id)
            except:
                res = json.dumps({'code':1, 'status':'Error', 'message': 'No destination with this id', 'type': 'null', 'content': 'null'})
                return StreamingHttpResponse(res, content_type="application/json")
        else:
            try:
                target = Targets.objects.get(slug=t_id)
            except:
                res = json.dumps({'code':1, 'status':'Error', 'message': 'No destination with this slug', 'type': 'null', 'content': 'null'})
                return StreamingHttpResponse(res, content_type="application/json")

        target_missions = Missions.objects.all().filter(target=target)
           
        serializer = MissionsSerializer(target_missions, many=True)
        return JSONResponse(serializer.data)
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint', 'type': 'null', 'content': 'null'}
        return JSONResponse(mex)

@csrf_exempt
@api_view(['GET'])
def single_component(request, c_id):
    """
    Get single PL and BUS Components from component id
    'pbtype' is an id from PL and BUS types.
    """
    if request.method == 'GET':
        mix = PayloadBusComps.objects.get(id=c_id)
        serializer = PayloadBusCompsSerializer(mix, many=False)
        return JSONResponse(serializer.data)
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint', 'type': 'null', 'content': 'null'}
        return JSONResponse(mex)

@csrf_exempt
@api_view(['GET'])
def components_list(request):
    """
    List of all PL and BUS components.
    'pbtype' contains ids from PL and BUS types.
    """
    if request.method == 'GET':
        mix = PayloadBusComps.objects.all().order_by('pbtype')
        serializer = PayloadBusCompsSerializer(mix, many=True)
        return JSONResponse(serializer.data)
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint', 'type': 'null', 'content': 'null'}
        return JSONResponse(mex)

@csrf_exempt
@api_view(['GET'])
def single_pb_type(request, type_id):
    """
    Get single PL and BUS TYPES from type id
    Useful to check the 'pbtype' from Components.
    """
    if request.method == 'GET':
        mix = PayloadBusTypes.objects.get(id=type_id)
        serializer = PayloadBusTypesSerializer(mix, many=False)
        return JSONResponse(serializer.data)
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint', 'type': 'null', 'content': 'null'}
        return JSONResponse(mex)

@csrf_exempt
@api_view(['GET'])
def pb_list(request):
    """
    List of all PL and BUS TYPES.
    Useful to check the 'pbtype' from Components.
    """
    if request.method == 'GET':
        mix = PayloadBusTypes.objects.all()
        serializer = PayloadBusTypesSerializer(mix, many=True)
        return JSONResponse(serializer.data)
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint', 'type': 'null', 'content': 'null'}
        return JSONResponse(mex)

@csrf_exempt
@api_view(['GET'])
def data_by_comps(request, comp_id):
    """
    List of SciData filtered by components.
    Useful to retrieve data about certain components.
    """
    if request.method == 'GET':
        mix = SciData.objects.all().filter(component=comp_id)
        serializer = SciDataSerializer(mix, many=True)
        return JSONResponse(serializer.data)
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint', 'type': 'null', 'content': 'null'}
        return JSONResponse(mex)

@csrf_exempt
@api_view(['GET'])
def data_by_target_by_comps(request, t_id, c_id):
    """
    List of SciData filtered by mission.
    Useful to retrieve data about certain mission.
    """
    if request.method == 'GET':
        mix = SciData.objects.all().filter(component=c_id).filter(mission__target__id=t_id).exclude(data_type=0)[2:5]
        serializer = SciDataSerializer(mix, many=True)
        return JSONResponse(serializer.data)
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint', 'type': 'null', 'content': 'null'}
        return JSONResponse(mex)

@csrf_exempt
@api_view(['GET'])
def data_by_target(request, t_id):
    """
    List of SciData filtered by target.
    Useful to retrieve data about certain mission.
    """
    if request.method == 'GET':
        mix = SciData.objects.all().filter(mission__target__id=t_id)
        serializer = SciDataSerializer(mix, many=True)
        return JSONResponse(serializer.data)
    else:
        mex = {'status': 'Error', 'code': 1, 'message': 'NO POST, PUT or DELETE for this endpoint', 'type': 'null', 'content': 'null'}
        return JSONResponse(mex)


def arbormap(request, state):
    from django.template import RequestContext
    payloads = PayloadBusComps.objects.all().filter(category='payload')
    if request.method == 'GET':
        if state == '0':
            params = dict()
            params['payloads'] = payloads
            params['state'] = state
            return render_to_response('webapp/map.html', params,
                              context_instance=RequestContext(request))

        else:
            params = dict()
            params['payloads'] = payloads
            params['state'] = state

            data = {"edges": {}, "nodes": {}}

            ### Pre-create nodes and empty edges for Components ###
            comp = payloads.filter(id=int(state)).first()
            c_key = 'P'+str(comp.id)
            c_value = {"label": comp.name, "id": c_key, "type": "component"}
            data['nodes'][c_key] = c_value
            data['edges'][c_key] = dict()

            fields = SciData.objects.all().filter(data_type=4)
            if not fields:
                raise Http404

            ### Pre-create nodes and empty edges for Fields ###
            for field in fields:
                f_key = 'F'+str(field.id)
                data['edges'][f_key] = dict()

            ### Query Data ###
            scidata = SciData.objects.all().filter(component__id=int(state))
            if not scidata:
                raise Http404

            print scidata.count()
            for s in scidata:
                ### Processing a single Datum 's' ###
                d_key = None
                m_key = None
                f_key = None
                f_key_in_c = None

                ### Datum is not of type Field ###
                if s.data_type != 4:
                    d_key = 'D'+str(s.id)
                    header = s.header[0:25]
                    d_value = {"label": header, "id": d_key, "type": "datum"}
                    data['nodes'][d_key] = d_value

                    print c_key
                    print d_key

                    ### Datum has a relation to a Mission ###
                    if s.mission is not None:
                        m_key = 'M'+str(s.mission.id)
                        m_value = {"label": s.mission.codename, "id": m_key, "type": "mission"}
                        if m_key not in data['edges'].keys():
                            data['edges'][m_key] = dict()
                        if m_key not in data['nodes'].keys():
                            data['nodes'][m_key] = m_value
                        data['edges'][m_key][d_key] = d_value  # M < D

                    ### Datum has a relation to a Field ###
                    if s.related_to is not None:
                        f_key_in_c = 'F'+str(s.related_to.id)
                        header_f = s.related_to.header
                        f_value = {"label": header_f, "id": f_key_in_c, "type": "field"}
                        data['nodes'][f_key_in_c] = f_value
                        data['edges'][c_key][f_key_in_c] = f_value
                        data['edges'][f_key_in_c][d_key] = d_value
                    else:
                        # Basic relation Component - Datum
                        data['edges'][c_key][d_key] = d_value

            for i in data['edges'].keys():
                if data['edges'][i] == {}:
                    del data['edges'][i]
            params['data'] = json.dumps(data)
            print params['data']

            return render_to_response('webapp/map.html', params,
                              context_instance=RequestContext(request))


def cytomap(request, state):
    from django.template import RequestContext
    payloads = PayloadBusComps.objects.all().filter(category='payload')
    if request.method == 'GET':
        if state == '0':
            params = dict()
            params['payloads'] = payloads
            params['state'] = state
            return render_to_response('webapp/cytomap.html', params,
                              context_instance=RequestContext(request))

        else:
            params = dict()
            params['payloads'] = payloads
            params['state'] = state

            data = {"edges": [], "nodes": []}

            ### Pre-create nodes and empty edges for Component ###
            comp = payloads.filter(id=int(state)).first()
            c_key = 'P'+str(comp.id)
            c_node = {"data": {"name": comp.name, "id": c_key, "type": "component", "weight": 99},
                      "grabbable": False }
            data['nodes'].append(c_node)

            fields = SciData.objects.all().filter(data_type=4)
            if not fields:
                raise Http404

            ### Pre-create nodes and empty edges for Fields ###
            for field in fields:
                f_key = 'F'+str(field.id)
                f_node = {"data": {"name": field.header, "id": f_key, "type": "field", "weight": 68}}
                data['nodes'].append(f_node)
                f_edge = {"data": {"source": f_key, "target": c_key, "weight": 68}}
                data['edges'].append(f_edge)



            ### Query Data ###
            scidata = SciData.objects.all().filter(component__id=int(state))
            if not scidata:
                raise Http404

            print scidata.count()
            for s in scidata:
                ### Processing a single Datum 's' ###
                d_key = None
                m_key = None
                f_key = None
                f_key_in_c = None

                ### Datum is not of type Field ###
                if s.data_type != 4:
                    d_key = 'D'+str(s.id)
                    header = s.header
                    d_node = {"data": {"name": header, "id": d_key, "href": s.body, "type": "datum", "weight": 50}}
                    d_edge = {"data": {"source": d_key, "target": c_key, "weight": 50}}
                    data['nodes'].append(d_node)


                    #print c_key
                    #print d_key
                    ### Datum has a relation to a Mission ###
                    if s.mission is not None:
                        m_link = "/webapp/data/missions/details/"+str(s.mission.id)
                        m_key = 'M'+str(s.mission.id)
                        m_name = str(s.mission.codename)+" - "+str(s.mission.target)
                        m_node = {"data": {"name": m_name, "id": m_key, "href": m_link, "type": "mission", "weight": 12}}
                        m_edge = {"data": {"source": m_key, "target": d_key, "weight": 12}}
                        if m_node not in data['nodes']:
                            data['nodes'].append(m_node)
                        if m_edge not in data['edges']:
                            data['edges'].append(m_edge)  # M < D

                    ### Datum has a relation to a Field ###
                    if s.related_to is not None:
                        f_key = 'F'+str(s.related_to.id)

                        data['edges'].append({"data": {"source": d_key, "target": f_key, "weight": 68}})
                    else:
                        # Basic relation Component - Datum
                        data['edges'].append(d_edge)

            '''for i in data['edges']:
                if data['edges'][i] == {}:
                    del data['edges'][i]'''
            params['data'] = json.dumps(data)
            #print params['data']

            return render_to_response('webapp/cytomap.html', params,
                              context_instance=RequestContext(request))