import json
from django.http import HttpResponse, StreamingHttpResponse
#import random
from django.shortcuts import render_to_response
from django.http import Http404

'''
import verity tables for mission's checking
'''
from data.Bodies_vs_Mission import destinations       #1
from data.Missions_vs_PL import mission_type          #2
from data.Dist_vs_Bus import bus_vs_dist              #3
from data.Mission_vs_Bus import bus_vs_mission_type   #4
from data.PL_vs_Bus import pl_vs_bus_type             #5
from data.NPL_vs_Bus import npl_vs_bus_type           #6
from data.Bus_vs_Bus import bus_vs_bus                #7


def simulation(request):

    ''' 
    GET example: 
    /simulation/?
        destination=mars
        &mission=deep_space_obs
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

    # 1 check compatibility planet/mission  
    if usr_planet[usr_mission_slug] != True :
        results = {'code': 1, 'status': 'Error', 'message':'Error in simulation', 
                   'type': 'Error in mission type ' + usr_mission_slug, 'content': usr_planet[usr_mission_slug][1] }
        return StreamingHttpResponse(json.dumps(results), content_type="application/json")
        

    # take PAYLOADS from URL and dump into a list
    components = [k for k,v in request.GET.iteritems() if v == 'true']
    

    #components = ['opt_sensor', 'radio_sensor', 'spectrometer', 'probe', 'amplifier']
    #comp_samples = random.sample(components, random.randint(1, len(components)))

    # 2 check PAYLOAD/MISSION compatibility - mission_type
    for e in components:
        #print e
        for k in mission_type:
            #print k
            if k['slug'] == usr_mission_slug:
                if k[e] != True: 
                    results = { 'code': 1, 'status': 'Error', 'message':'Error in simulation', 
                                'type': 'Error in component ' + e, 'content': k[e][1] }
                    return StreamingHttpResponse(json.dumps(results), content_type="application/json") 

    
    # get BUS components from URL
    busAll = {}
    for k,v in request.GET.iteritems():
        if v == 'bustrue':
            busAll[k] = True

    
    usr_distance = float(usr_planet['distance'])

    if len(busAll) != 0:
        # check if no payload is choosen for the BUS
        if len(components) == 0:
            results = { 'code':1, 'status': 'Error', 'message':'Error in simulation', 
                                    'type': 'Error in payload number check', 'content': 'Does it makes sense to send a BUS with no payload?' }
            return StreamingHttpResponse(json.dumps(results), content_type="application/json")

        for k,v in busAll.iteritems():
            # 3 check if BUS components are compatible with DISTANCE
            for e in bus_vs_dist:
                j = float(e['range_max'])
                
                # return StreamingHttpResponse(json.dumps(j), content_type="application/json")
                if j < usr_distance:
                    pass
                else:
                    print e['name'], j, usr_distance
                    if e[k] != v:
                        results = { 'code':1, 'status': 'Error', 'message':'Error in simulation', 
                                    'type': 'Error in BUS vs distance check ' + k, 'content': 'null' }
                        return StreamingHttpResponse(json.dumps(results), content_type="application/json")
                    break

            # 4 check if BUS systems and subsystems are compatible with type of MISSION - bus_vs_mission_type
     
            for f in bus_vs_mission_type:
                if f['slug'] == usr_mission_slug:
                        if f[k] != True:
                            results = {'code': 1, 'status': 'Error', 'message':'Error in simulation', 
                                       'type': 'Error in BUS in system ' + k, 'content': f[k][1] }
                            return StreamingHttpResponse(json.dumps(results), content_type="application/json")

            # 5 check if the PAYLOAD/BUS choices are compatible - pl_vs_bus
            for g in components: 
                for x in pl_vs_bus_type:
                  #print k
                  if x['slug'] == g:
                      if x[k] != True: 
                        results = { 'code': 1, 'status': 'Error', 'message':'Error in simulation', 
                                    'type': 'Error in payload/bus compatibility', 'content': x[k][1] }
                        return StreamingHttpResponse(json.dumps(results), content_type="application/json")

            # 6 check if the NUMBER of PAYLOADS choices are compatible - npl_vs_bus
            for h in npl_vs_bus_type:
                j = int(h['check'])
                
                # return StreamingHttpResponse(json.dumps(j), content_type="application/json")
                if j == len(busAll):
                    if h[k] != True:
                        results = { 'code':1, 'status': 'Error', 'message':'Error in simulation', 
                                    'type': 'Error in number of payloads check ', 'content': h[k][1] }
                        return StreamingHttpResponse(json.dumps(results), content_type="application/json")
                    
            # 7 check if the payload is compatible - bus_vs_bus

            for i in bus_vs_bus:
                if i['slug'] == usr_mission_slug:
                    for k,v in busAll.iteritems():
                        if i[k] != v:
                            results = { 'message':'Error in simulation', 'type': 'Error in BUS vs payload check ' + k,
                                       'content': i[k][1], 'code':1, 'status': 'Error' }
                            return StreamingHttpResponse(json.dumps(results), content_type="application/json")

    results = { 'code':0, 'status':'OK', 'message': 'Mission is way to go!', 'type': 'cheer', 'content': 'null' }
    return StreamingHttpResponse(json.dumps(results), content_type="application/json") 

        



