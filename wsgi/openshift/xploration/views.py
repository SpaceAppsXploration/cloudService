import json
from django.http import StreamingHttpResponse
import random
from django.shortcuts import render_to_response
from django.http import Http404

from tables_Bodies import destinations
from tables_Missions import mission_type
from tables_BusVsMission import bus_vs_mission_type

# Create your views here.

def home(request):
    js = {'status': 'Coming Soon...', 'response': 200, 'code': 0}
    js = json.dumps(js)
    
    params = {}
    params['keywords'] = 'space journey satellites exploration solar system simulation play'
    params['status'] = js
    return render_to_response('home/home.html', params)

def Mars(request):
    js = [
       {
          "headlines":"/news/archive.cfm?Mission=Odyssey",
          "image_url":"/missions/images/miss-odyssey.jpg",
          "goals":"Mars Odyssey is an orbiter carrying science experiments designed to make global observations of Mars to improve our understanding of the planet's climate and geologic history, including the search for water and evidence of life-sustaining environments.",
          "link":"http://marsprogram.jpl.nasa.gov/odyssey/",
          "mission_type":"null",
          "code":"2001 Mars Odyssey",
          "hashed":"Odyssey",
          "accomplished":"Mars Odyssey provided stunning images and crucial science far beyond its planned 917-day mission. The orbiter made valuable global observations of Martian climate, geology and mineralogy. It mapped the elemental distribution of hydrogen, silicon, iron, potassium, thorium and chlorine on the Martian surface. Odyssey also determined that radiation in low-Mars orbit -- an essential piece of information for eventual human exploration because of its potential health effects -- is twice that in low-Earth orbit.",
          "destination":"Mars"
       },
       {
          "headlines":"/news/archive.cfm?Mission=MarsExpress",
          "image_url":"/missions/images/miss-marsexpress.jpg",
          "goals":"The European Space Agency's Mars Express was designed to study the geology, atmosphere, surface environment, history of water and potential for life on Mars. It also carried Great Britain's ",
          "link":"http://www.esa.int/Our_Activities/Space_Science/Mars_Express",
          "mission_type":"null",
          "code":"Mars Express",
          "hashed":"MarsExpress",
          "accomplished":"Mars Express was Europe's first mission to another planet. It provided subsurface measurements with the first radar instrument ever flown to Mars, and discovered underground water-ice deposits. It sent back mineralogical evidence for the presence of liquid water throughout Martian history and studied the density of the Martian crust in detail. The orbiter's unique orbit also has allowed it to make up-closed studies of Phobos, the larger of Mars' two moons. The mission has been extended several times.",
          "destination":"Mars"
       },
       {
          "headlines":"/news/archive.cfm?Mission=MER",
          "image_url":"/missions/images/miss-mer_a.jpg",
          "goals":"ASA's Mars Exploration Rovers - Spirit and its twin Opportunity - were designed to study the history of climate and water at sites on Mars where conditions may once have been favorable to life. Each rover is equipped with a suite of science instruments to read the geologic record at each site, to investigate what role water played there and to determine how suitable the conditions would have been for life.",
          "link":"http://marsrovers.jpl.nasa.gov/home/index.html",
          "mission_type":"null",
          "code":"Mars Exploration Rovers",
          "hashed":"MER",
          "accomplished":"oth rovers far exceeded their design specifications and returned science results that transformed our understanding of Mars.",
          "destination":"Mars"
       },
       {
          "headlines":"/news/archive.cfm?Mission=MRO",
          "image_url":"/missions/images/miss-mro.gif",
          "goals":"Mars Reconnaissance Orbiter (MRO) is designed to track changes in the water and dust in Mars' atmosphere, look for more evidence of ancient seas and hot springs and peer into past Martian climate changes by studying surface minerals and layering. The orbiter carries a powerful camera capable of taking sharp images of surface features the size of a beach ball. The orbiter also serves as a data  relay station for other Mars missions.",
          "link":"http://marsprogram.jpl.nasa.gov/mro/",
          "mission_type":"null",
          "code":"Mars Recon Orbiter",
          "hashed":"MRO",
          "accomplished":"Among the mission's major findings is that the action of water on and near the surface of Mars occurred for hundreds of millions of years. This activity was at least regional and possibly global in extent, though possibly intermittent. The spacecraft has also observed signatures of a variety of watery environments, some acidic, some alkaline, which increase the possibility that there are places on Mars that could reveal evidence of past life, if it ever existed. MRO also broke data transmission records, surpassing all other previous Mars missions.",
          "destination":"Mars"
       }
    ]

    js = json.dumps(js)

    return StreamingHttpResponse(js, content_type="application/json")

def test(request):
    js = {'code': 0, 'status': 'OK', 'response': 200}
    js = json.dumps(js)

    return StreamingHttpResponse(js, content_type="application/json")

def simulation(request):

    ''' 
    GET example: 
    /simulation/?
        destination=mars
        &mission=prop_chem
        &opt_sensor=true
        &radio_sensor=falses
        &pectrometer=true probe=true
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

    
    if usr_planet[usr_mission_slug] != True :
        results = {'code': 1, 'Error': 'Error in mission type ' + usr_mission_slug }
        return StreamingHttpResponse(json.dumps(results), content_type="application/json")
        

    # take components from URL and dump into a list
    components = [k for k,v in request.GET.iteritems() if v == 'true']
    

    #components = ['opt_sensor', 'radio_sensor', 'spectrometer', 'probe', 'amplifier']
    #comp_samples = random.sample(components, random.randint(1, len(components)))


    for e in components:
        #print e
        for k in mission_type:
            #print k
            if k['slug'] == usr_mission_slug:
                if k[e] != True: 
                    results = { 'code': 1, 'Error': 'Error in component ' + e }
                    return StreamingHttpResponse(json.dumps(results), content_type="application/json") 

    

    #############################


    
    
    busAll = {}
    for k,v in request.GET.iteritems():
        if v == 'bustrue':
            busAll[k] = True

    if len(busAll) != 0:
      for e in bus_vs_mission_type:
        if e['slug'] == usr_mission_slug:
            for k,v in busAll.iteritems():
                if e[k] != v:
                    results = {'code': 1, 'Error': 'Error in BUS in system ' + k }
                    return StreamingHttpResponse(json.dumps(results), content_type="application/json")

    bus_vs_dist = []

    dist1 = {}
    dist1['name'] = 'Dist1'
    dist1['slug'] = 'dist1'
    dist1['range_min'] = 0
    dist1['range_max'] = 0.8
    dist1['therm_active'] = True
    dist1['therm_passive'] = False
    dist1['pow_prim_panels'] = True
    dist1['pow_prim_rtg'] = False
    dist1['pow_sec_batt'] = True
    dist1['pow_sec_fc'] = True
    dist1['comm_mono'] = False
    dist1['comm_omni'] = True
    dist1['aodcs_robust'] = True
    dist1['aodcs_simple'] = True
    dist1['prop_electr'] = True
    dist1['prop_chem'] = True
    dist1['cdh_standard'] = True
    dist1['cdh_optim'] = True
    dist1['struct_stand'] = True
    dist1['struct_high_resist'] = True

    bus_vs_dist.append(dist1)

    dist2 = {}
    dist2['name'] = 'Dist2'
    dist2['slug'] = 'dist2'
    dist2['range_min'] = 0.8
    dist2['range_max'] = 1.6
    dist2['therm_active'] = False
    dist2['therm_passive'] = True
    dist2['pow_prim_panels'] = True
    dist2['pow_prim_rtg'] = False
    dist2['pow_sec_batt'] = True
    dist2['pow_sec_fc'] = True
    dist2['comm_mono'] = False
    dist2['comm_omni'] = True
    dist2['aodcs_robust'] = True
    dist2['aodcs_simple'] = True
    dist2['prop_electr'] = True
    dist2['prop_chem'] = True
    dist2['cdh_standard'] = True
    dist2['cdh_optim'] = True
    dist2['struct_stand'] = True
    dist2['struct_high_resist'] = True

    bus_vs_dist.append(dist2)

    dist3 = {}
    dist3['name'] = 'Dist3'
    dist3['slug'] = 'dist3'
    dist3['range_min'] = 1.6
    dist3['range_max'] = 3
    dist3['therm_active'] = True
    dist3['therm_passive'] = False
    dist3['pow_prim_panels'] = True
    dist3['pow_prim_rtg'] = False
    dist3['pow_sec_batt'] = True
    dist3['pow_sec_fc'] = True
    dist3['comm_mono'] = True
    dist3['comm_omni'] = False
    dist3['aodcs_robust'] = True
    dist3['aodcs_simple'] = True
    dist3['prop_electr'] = True
    dist3['prop_chem'] = True
    dist3['cdh_standard'] = True
    dist3['cdh_optim'] = True
    dist3['struct_stand'] = False
    dist3['struct_high_resist'] = True

    bus_vs_dist.append(dist3)

    dist4 = {}
    dist4['name'] = 'Dist4'
    dist4['slug'] = 'dist4'
    dist4['range_min'] = 3
    dist4['range_max'] = 5.5
    dist4['therm_active'] = True
    dist4['therm_passive'] = False
    dist4['pow_prim_panels'] = True
    dist4['pow_prim_rtg'] = True
    dist4['pow_sec_batt'] = True
    dist4['pow_sec_fc'] = True
    dist4['comm_mono'] = True
    dist4['comm_omni'] = False
    dist4['aodcs_robust'] = True
    dist4['aodcs_simple'] = True
    dist4['prop_electr'] = True
    dist4['prop_chem'] = True
    dist4['cdh_standard'] = True
    dist4['cdh_optim'] = True
    dist4['struct_stand'] = True
    dist4['struct_high_resist'] = True

    bus_vs_dist.append(dist4)

    dist5 = {}
    dist5['name'] = 'Dist5'
    dist5['slug'] = 'dist5'
    dist5['range_min'] = 5.5
    dist5['range_max'] = 50
    dist5['therm_active'] = True
    dist5['therm_passive'] = False
    dist5['pow_prim_panels'] = False
    dist5['pow_prim_rtg'] = True
    dist5['pow_sec_batt'] = True
    dist5['pow_sec_fc'] = True
    dist5['comm_mono'] = True
    dist5['comm_omni'] = False
    dist5['aodcs_robust'] = True
    dist5['aodcs_simple'] = True
    dist5['prop_electr'] = True
    dist5['prop_chem'] = True
    dist5['cdh_standard'] = True
    dist5['cdh_optim'] = True
    dist5['struct_stand'] = True
    dist5['struct_high_resist'] = True

    bus_vs_dist.append(dist5)

    usr_distance = usr_planet['distance']


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


    bus_vs_bus = []

    aodcs_robust = {}
    aodcs_robust['name'] = 'AODCS Robust'
    aodcs_robust['slug'] = 'aodcs_robust'
    aodcs_robust['therm_active'] = False
    aodcs_robust['therm_passive'] = True
    aodcs_robust['pow_prim_panels'] = True
    aodcs_robust['pow_prim_rtg'] = True
    aodcs_robust['pow_sec_batt'] = True
    aodcs_robust['pow_sec_fc'] = True
    aodcs_robust['comm_mono'] = True
    aodcs_robust['comm_omni'] = True
    aodcs_robust['aodcs_robust'] = True
    aodcs_robust['aodcs_simple'] = False
    aodcs_robust['prop_electr'] = True
    aodcs_robust['prop_chem'] = True
    aodcs_robust['cdh_standard'] = True
    aodcs_robust['cdh_optim'] = True
    aodcs_robust['struct_stand'] = True
    aodcs_robust['struct_high_resist'] = True

    bus_vs_bus.append(aodcs_robust)



    aodcs_simple = {}
    aodcs_simple['name'] = 'AODCS Simple'
    aodcs_simple['slug'] = 'aodcs_simple'
    aodcs_simple['therm_active'] = True
    aodcs_simple['therm_passive'] = False
    aodcs_simple['pow_prim_panels'] = False
    aodcs_simple['pow_prim_rtg'] = True
    aodcs_simple['pow_sec_batt'] = True
    aodcs_simple['pow_sec_fc'] = True
    aodcs_simple['comm_mono'] = False
    aodcs_simple['comm_omni'] = True
    aodcs_simple['aodcs_robust'] = False
    aodcs_simple['aodcs_simple'] = True
    aodcs_simple['prop_electr'] = True
    aodcs_simple['prop_chem'] = False
    aodcs_simple['cdh_standard'] = True
    aodcs_simple['cdh_optim'] = True
    aodcs_simple['struct_stand'] = True
    aodcs_simple['struct_high_resist'] = True

    bus_vs_bus.append(aodcs_simple)



    prop_elect = {}
    prop_elect['name'] = 'Electric Propulsion'
    prop_elect['slug'] = 'prop_elect'
    prop_elect['therm_active'] = True
    prop_elect['therm_passive'] = True
    prop_elect['pow_prim_panels'] = True
    prop_elect['pow_prim_rtg'] = True
    prop_elect['pow_sec_batt'] = True
    prop_elect['pow_sec_fc'] = False
    prop_elect['comm_mono'] = True
    prop_elect['comm_omni'] = True
    prop_elect['aodcs_robust'] = True
    prop_elect['aodcs_simple'] = True
    prop_elect['prop_electr'] = True
    prop_elect['prop_chem'] = False
    prop_elect['cdh_standard'] = True
    prop_elect['cdh_optim'] = True
    prop_elect['struct_stand'] = True
    prop_elect['struct_high_resist'] = True

    bus_vs_bus.append(prop_elect)



    prop_chem = {}
    prop_chem['name'] = 'Chemical Propulsion'
    prop_chem['slug'] = 'prop_chem'
    prop_chem['therm_active'] = True
    prop_chem['therm_passive'] = True
    prop_chem['pow_prim_panels'] = True
    prop_chem['pow_prim_rtg'] = True
    prop_chem['pow_sec_batt'] = True
    prop_chem['pow_sec_fc'] = True
    prop_chem['comm_mono'] = True
    prop_chem['comm_omni'] = True
    prop_chem['aodcs_robust'] = True
    prop_chem['aodcs_simple'] = False
    prop_chem['prop_electr'] = False
    prop_chem['prop_chem'] = True
    prop_chem['cdh_standard'] = True
    prop_chem['cdh_optim'] = True
    prop_chem['struct_stand'] = True
    prop_chem['struct_high_resist'] = True

    bus_vs_bus.append(prop_chem)



    cdh_standard = {}
    cdh_standard['name'] = 'CDH Standard'
    cdh_standard['slug'] = 'cdh_standard'
    cdh_standard['therm_active'] = True
    cdh_standard['therm_passive'] = True
    cdh_standard['pow_prim_panels'] = True
    cdh_standard['pow_prim_rtg'] = True
    cdh_standard['pow_sec_batt'] = True
    cdh_standard['pow_sec_fc'] = True
    cdh_standard['comm_mono'] = True
    cdh_standard['comm_omni'] = False
    cdh_standard['aodcs_robust'] = True
    cdh_standard['aodcs_simple'] = True
    cdh_standard['prop_electr'] = True
    cdh_standard['prop_chem'] = True
    cdh_standard['cdh_standard'] = True
    cdh_standard['cdh_optim'] = False
    cdh_standard['struct_stand'] = True
    cdh_standard['struct_high_resist'] = True

    bus_vs_bus.append(cdh_standard)



    cdh_optim = {}
    cdh_optim['name'] = 'CDH Optimized'
    cdh_optim['slug'] = 'cdh_optim'
    cdh_optim['therm_active'] = True
    cdh_optim['therm_passive'] = True
    cdh_optim['pow_prim_panels'] = True
    cdh_optim['pow_prim_rtg'] = True
    cdh_optim['pow_sec_batt'] = True
    cdh_optim['pow_sec_fc'] = True
    cdh_optim['comm_mono'] = True
    cdh_optim['comm_omni'] = True
    cdh_optim['aodcs_robust'] = True
    cdh_optim['aodcs_simple'] = True
    cdh_optim['prop_electr'] = True
    cdh_optim['prop_chem'] = True
    cdh_optim['cdh_standard'] = False
    cdh_optim['cdh_optim'] = True
    cdh_optim['struct_stand'] = True
    cdh_optim['struct_high_resist'] = True

    bus_vs_bus.append(cdh_optim)



    struct_stand = {}
    struct_stand['name'] = 'Standard Structure'
    struct_stand['slug'] = 'struct_stand'
    struct_stand['therm_active'] = True
    struct_stand['therm_passive'] = True
    struct_stand['pow_prim_panels'] = True
    struct_stand['pow_prim_rtg'] = False
    struct_stand['pow_sec_batt'] = True
    struct_stand['pow_sec_fc'] = True
    struct_stand['comm_mono'] = True
    struct_stand['comm_omni'] = True
    struct_stand['aodcs_robust'] = True
    struct_stand['aodcs_simple'] = True
    struct_stand['prop_electr'] = True
    struct_stand['prop_chem'] = True
    struct_stand['cdh_standard'] = True
    struct_stand['cdh_optim'] = True
    struct_stand['struct_stand'] = True
    struct_stand['struct_high_resist'] = False

    bus_vs_bus.append(struct_stand)


    struct_high_resist = {}
    struct_high_resist['name'] = 'Standard Structure'
    struct_high_resist['slug'] = 'struct_high_resist'
    struct_high_resist['therm_active'] = True
    struct_high_resist['therm_passive'] = True
    struct_high_resist['pow_prim_panels'] = True
    struct_high_resist['pow_prim_rtg'] = True
    struct_high_resist['pow_sec_batt'] = True
    struct_high_resist['pow_sec_fc'] = True
    struct_high_resist['comm_mono'] = True
    struct_high_resist['comm_omni'] = True
    struct_high_resist['aodcs_robust'] = True
    struct_high_resist['aodcs_simple'] = True
    struct_high_resist['prop_electr'] = True
    struct_high_resist['prop_chem'] = True
    struct_high_resist['cdh_standard'] = True
    struct_high_resist['cdh_optim'] = True
    struct_high_resist['struct_stand'] = False
    struct_high_resist['struct_high_resist'] = True

    bus_vs_bus.append(struct_high_resist)

    if len(busAll) != 0:
      for e in bus_vs_bus:
        if e['slug'] == usr_mission_slug:
            for k,v in busAll.iteritems():
                if e[k] != v:
                    results = { 'code':1, 'Error': 'Error in BUS in payload check ' + k }
                    return StreamingHttpResponse(json.dumps(results), content_type="application/json")

    results = { 'code':0, 'status':'OK - Mission is possible' }
    return StreamingHttpResponse(json.dumps(results), content_type="application/json") 

        



