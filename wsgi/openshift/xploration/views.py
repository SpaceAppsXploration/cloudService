import json
from django.http import StreamingHttpResponse
import random
from django.shortcuts import render_to_response

# Create your views here.

def home(request):
    js = {'status': 'OK', 'response': 200}
    js = json.dumps(js)

    return StreamingHttpResponse(js, content_type="application/json")

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
    js = {'status': 'OK', 'response': 200}
    js = json.dumps(js)

    return StreamingHttpResponse(js, content_type="application/json")

def simulation(request):

    # GET example: /simulation/?planet=mars&mission=prop-chem&opt_sensor=true&radio_sensor=false&spectrometer=true& probe=true&amplifierfier=false

    #js = request.GET
    #js = {'status': 'OK', 'response': 200}
    #js = json.dumps(js)

    #return StreamingHttpResponse(js, content_type="application/json")

    planets = []
    mercury = {}
    mercury['name'] = 'Mercury'
    mercury['slug'] = 'mercury'
    mercury['distance'] = 0.4
    mercury['earth_obs'] = False
    mercury['cel_body_obs'] = True
    mercury['deep_space_obs'] = False
    mercury['atm_analysis'] = True
    mercury['sample_collect'] = True
    mercury['telecom'] = False

    planets.append(mercury)

    venus = {}
    venus['name'] = 'Venus'
    venus['slug'] = 'venus'
    venus['distance'] = 0.7
    venus['earth_obs'] = False
    venus['cel_body_obs'] = True
    venus['deep_space_obs'] = False
    venus['atm_analysis'] = True
    venus['sample_collect'] = True
    venus['telecom'] = False

    planets.append(venus)

    earth = {}
    earth['name'] = 'Earth'
    earth['slug'] = 'earth'
    earth['distance'] = 1
    earth['earth_obs'] = True
    earth['cel_body_obs'] = False
    earth['deep_space_obs'] = True
    earth['atm_analysis'] = True
    earth['sample_collect'] = False
    earth['telecom'] = True

    planets.append(earth)

    moon = {}
    moon['name'] = 'Moon'
    moon['slug'] = 'moon'
    moon['distance'] = 1
    moon['earth_obs'] = False
    moon['cel_body_obs'] = True
    moon['deep_space_obs'] = False
    moon['atm_analysis'] = False
    moon['sample_collect'] = True
    moon['telecom'] = False

    planets.append(moon)

    mars = {}
    mars['name'] = 'Mars'
    mars['slug'] = 'mars'
    mars['distance'] = 1.5
    mars['earth_obs'] = False
    mars['cel_body_obs'] = True
    mars['deep_space_obs'] = False
    mars['atm_analysis'] = True
    mars['sample_collect'] = True
    mars['telecom'] = False

    planets.append(mars)

    asteroids = {}
    asteroids['name'] = 'Asteroids'
    asteroids['slug'] = 'asteroids'
    asteroids['distance'] = 2.8
    asteroids['earth_obs'] = False
    asteroids['cel_body_obs'] = True
    asteroids['deep_space_obs'] = False
    asteroids['atm_analysis'] = False
    asteroids['sample_collect'] = True
    asteroids['telecom'] = False

    planets.append(asteroids)

    jupiter = {}
    jupiter['name'] = 'Jupiter'
    jupiter['slug'] = 'jupiter'
    jupiter['distance'] = 5.2
    jupiter['earth_obs'] = False
    jupiter['cel_body_obs'] = True
    jupiter['deep_space_obs'] = False
    jupiter['atm_analysis'] = True
    jupiter['sample_collect'] = True
    jupiter['telecom'] = False

    planets.append(jupiter)

    saturn = {}
    saturn['name'] = 'Saturn'
    saturn['slug'] = 'saturn'
    saturn['distance'] = 9.5 
    saturn['earth_obs'] = False
    saturn['cel_body_obs'] = True
    saturn['deep_space_obs'] = False
    saturn['atm_analysis'] = True
    saturn['sample_collect'] = True
    saturn['telecom'] = False

    planets.append(saturn)

    uranus = {}
    uranus['name'] = 'Uranus'
    uranus['slug'] = 'uranus'
    uranus['distance'] = 19.2
    uranus['earth_obs'] = False
    uranus['cel_body_obs'] = True
    uranus['deep_space_obs'] = False
    uranus['atm_analysis'] = True
    uranus['sample_collect'] = True
    uranus['telecom'] = False

    planets.append(uranus)

    neptune = {}
    neptune['name'] = 'Neptune'
    neptune['slug'] = 'neptune'
    neptune['distance'] = 30
    neptune['earth_obs'] = False
    neptune['cel_body_obs'] = True
    neptune['deep_space_obs'] = False
    neptune['atm_analysis'] = True
    neptune['sample_collect'] = True
    neptune['telecom'] = False

    planets.append(neptune)

    comets = {}
    comets['name'] = 'Comets'
    comets['slug'] = 'comets'
    comets['distance'] = 10
    comets['earth_obs'] = False
    comets['cel_body_obs'] = True
    comets['deep_space_obs'] = False
    comets['atm_analysis'] = False
    comets['sample_collect'] = True
    comets['telecom'] = False

    planets.append(comets)

    space = {}
    space['name'] = 'Space'
    space['slug'] = 'space'
    space['distance'] = 50
    space['earth_obs'] = False
    space['cel_body_obs'] = False
    space['deep_space_obs'] = True
    space['atm_analysis'] = False
    space['sample_collect'] = False
    space['telecom'] = False

    planets.append(space)





    #j = json.dumps(planets)

    #myFile = open('planets.json','w')
    #myFile.write(j)
    #myFile.close()


    mission_type = []

    earth_obs = {}
    earth_obs['name'] = 'Earth observation'
    earth_obs['slug'] = 'earth_obs'
    earth_obs['opt_sensor'] = True
    earth_obs['radio_sensor'] = True
    earth_obs['spectrometer'] = False
    earth_obs['probe'] = False
    earth_obs['amplifier'] = False

    mission_type.append(earth_obs)


    body_obs = {}
    body_obs['name'] = 'Body observation'
    body_obs['slug'] = 'cel_body_obs'
    body_obs['opt_sensor'] = True
    body_obs['radio_sensor'] = True
    body_obs['spectrometer'] = True
    body_obs['probe'] = False
    body_obs['amplifier'] = False

    mission_type.append(body_obs)

    space_obs = {}
    space_obs['name'] = 'Space observation'
    space_obs['slug'] = 'deep_space_obs'
    space_obs['opt_sensor'] = True
    space_obs['radio_sensor'] = True
    space_obs['spectrometer'] = True
    space_obs['probe'] = False
    space_obs['amplifier'] = True

    mission_type.append(space_obs)

    atm_analysis = {}
    atm_analysis['name'] = 'Atmospheric analysis'
    atm_analysis['slug'] = 'atm_analysis'
    atm_analysis['opt_sensor'] = True
    atm_analysis['radio_sensor'] = True
    atm_analysis['spectrometer'] = True
    atm_analysis['probe'] = False
    atm_analysis['amplifier'] = False

    mission_type.append(atm_analysis)

    sample_collect = {}
    sample_collect['name'] = 'Sample collection'
    sample_collect['slug'] = 'sample_collect'
    sample_collect['opt_sensor'] = True
    sample_collect['radio_sensor'] = False
    sample_collect['spectrometer'] = True
    sample_collect['probe'] = True
    sample_collect['amplifier'] = False

    mission_type.append(sample_collect)

    telecom = {}
    telecom['name'] = 'Telecommunication'
    telecom['slug'] = 'telecom'
    telecom['opt_sensor'] = False
    telecom['radio_sensor'] = False
    telecom['spectrometer'] = False
    telecom['probe'] = False
    telecom['amplifier'] = True

    mission_type.append(telecom)

    results = {}

    # /simulation/?destinatio=mars&mission=prop-chem&opt_sensor=true&radio_sensor=false&spectrometer=true& probe=true&amplifierfier=false

    usr_planet = request.GET['destination']

    for p in planets:
        if p['slug'] == usr_planet:
            usr_planet = p
    


    usr_mission_slug = request.GET['mission']
    #print  usr_planet['name'], usr_mission['name']


    if usr_planet[usr_mission_slug] != True :
        results['Error'] = [False, 'Errore in mission type ' + usr_mission_slug ]
        return StreamingHttpResponse(json.dumps(results), content_type="application/json")
        

    components = [k for k,v in request.GET.iteritems() if v == 'true']
    

    #components = ['opt_sensor', 'radio_sensor', 'spectrometer', 'probe', 'amplifier']
    # comp_samples = random.sample(components, random.randint(1, len(components)))


    for e in components:
        #print e
        for k in mission_type:
            #print k
            if k['slug'] == usr_mission_slug:
                if k[e] != True: 
                    results['Error'] = [False, 'Errore in component ' + e]
                    return StreamingHttpResponse(json.dumps(results), content_type="application/json") 

    

    #############################


    bus_vs_mission_type = []

    earth_obs = {}
    earth_obs['name'] = 'Earth observation'
    earth_obs['slug'] = 'earth_obs'
    earth_obs['therm_active'] = True
    earth_obs['therm_passive'] = True
    earth_obs['pow_prim_panels'] = True
    earth_obs['pow_prim_rtg'] = True
    earth_obs['pow_sec_batt'] = True
    earth_obs['pow_sec_fc'] = True
    earth_obs['comm_mono'] = True
    earth_obs['comm_omni'] = True
    earth_obs['aodcs_robust'] = True
    earth_obs['aodcs_simple'] = True
    earth_obs['prop_electr'] = True
    earth_obs['prop_chem'] = True
    earth_obs['cdh_standard'] = True
    earth_obs['cdh_optim'] = True
    earth_obs['struct_stand'] = True
    earth_obs['struct_high_resist'] = True

    bus_vs_mission_type.append(earth_obs)


    body_obs = {}
    body_obs['name'] = 'Body observation'
    body_obs['slug'] = 'body_obs'
    body_obs['therm_active'] = True
    body_obs['therm_passive'] = True
    body_obs['pow_prim_panels'] = True
    body_obs['pow_prim_rtg'] = True
    body_obs['pow_sec_batt'] = True
    body_obs['pow_sec_fc'] = True
    body_obs['comm_mono'] = True
    body_obs['comm_omni'] = True
    body_obs['aodcs_robust'] = True
    body_obs['aodcs_simple'] = True
    body_obs['prop_electr'] = True
    body_obs['prop_chem'] = True
    body_obs['cdh_standard'] = True
    body_obs['cdh_optim'] = True
    body_obs['struct_stand'] = True
    body_obs['struct_high_resist'] = True

    bus_vs_mission_type.append(body_obs)



    space_obs = {}
    space_obs['name'] = 'Space observation'
    space_obs['slug'] = 'space_obs'
    space_obs['therm_active'] = True
    space_obs['therm_passive'] = True
    space_obs['pow_prim_panels'] = True
    space_obs['pow_prim_rtg'] = True
    space_obs['pow_sec_batt'] = True
    space_obs['pow_sec_fc'] = True
    space_obs['comm_mono'] = True
    space_obs['comm_omni'] = True
    space_obs['aodcs_robust'] = True
    space_obs['aodcs_simple'] = True
    space_obs['prop_electr'] = True
    space_obs['prop_chem'] = True
    space_obs['cdh_standard'] = True
    space_obs['cdh_optim'] = True
    space_obs['struct_stand'] = True
    space_obs['struct_high_resist'] = True

    bus_vs_mission_type.append(space_obs)



    atm_analysis = {}
    atm_analysis['name'] = 'Athmosphere Analysis'
    atm_analysis['slug'] = 'atm_analysis'
    atm_analysis['therm_active'] = True
    atm_analysis['therm_passive'] = True
    atm_analysis['pow_prim_panels'] = True
    atm_analysis['pow_prim_rtg'] = True
    atm_analysis['pow_sec_batt'] = True
    atm_analysis['pow_sec_fc'] = True
    atm_analysis['comm_mono'] = True
    atm_analysis['comm_omni'] = True
    atm_analysis['aodcs_robust'] = True
    atm_analysis['aodcs_simple'] = True
    atm_analysis['prop_electr'] = True
    atm_analysis['prop_chem'] = True
    atm_analysis['cdh_standard'] = True
    atm_analysis['cdh_optim'] = True
    atm_analysis['struct_stand'] = True
    atm_analysis['struct_high_resist'] = True

    bus_vs_mission_type.append(atm_analysis)



    sample_collect = {}
    sample_collect['name'] = 'Samples Collection'
    sample_collect['slug'] = 'sample_collect'
    sample_collect['therm_active'] = True
    sample_collect['therm_passive'] = True
    sample_collect['pow_prim_panels'] = True
    sample_collect['pow_prim_rtg'] = True
    sample_collect['pow_sec_batt'] = True
    sample_collect['pow_sec_fc'] = True
    sample_collect['comm_mono'] = True
    sample_collect['comm_omni'] = True
    sample_collect['aodcs_robust'] = True
    sample_collect['aodcs_simple'] = False
    sample_collect['prop_electr'] = True
    sample_collect['prop_chem'] = True
    sample_collect['cdh_standard'] = True
    sample_collect['cdh_optim'] = True
    sample_collect['struct_stand'] = True
    sample_collect['struct_high_resist'] = True

    bus_vs_mission_type.append(sample_collect)



    telecom = {}
    telecom['name'] = 'Telecommunications'
    telecom['slug'] = 'telecom'
    telecom['therm_active'] = True
    telecom['therm_passive'] = True
    telecom['pow_prim_panels'] = True
    telecom['pow_prim_rtg'] = True
    telecom['pow_sec_batt'] = True
    telecom['pow_sec_fc'] = True
    telecom['comm_mono'] = True
    telecom['comm_omni'] = True
    telecom['aodcs_robust'] = True
    telecom['aodcs_simple'] = False
    telecom['prop_electr'] = True
    telecom['prop_chem'] = True
    telecom['cdh_standard'] = False
    telecom['cdh_optim'] = True
    telecom['struct_stand'] = True
    telecom['struct_high_resist'] = True

    bus_vs_mission_type.append(telecom)

    
    busAll = {}
    for k,v in request.GET.iteritems():
        if v == 'bustrue':
            busAll[k] = True

    for e in bus_vs_mission_type:
        if e['slug'] == usr_mission_slug:
            for k,v in busAll.iteritems():
                if e[k] != v:
                    results['Error'] = [False, 'Errore in BUS in system ' + k]
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
    dist1['c&dh_standard'] = True
    dist1['c&dh_optim'] = True
    dist1['struct_stand'] = True
    dist1['struct_high_resist'] = True

    bus_vs_dist.append(dist1)

    dist2 = {}
    dist1['name'] = 'Dist2'
    dist1['slug'] = 'dist2'
    dist1['range_min'] = 0.8
    dist1['range_max'] = 1.6
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
    dist2['c&dh_standard'] = True
    dist2['c&dh_optim'] = True
    dist2['struct_stand'] = True
    dist2['struct_high_resist'] = True

    bus_vs_dist.append(dist2)

    dist3 = {}
    dist3['name'] = 'Dist3'
    dist3['slug'] = 'dist3'
    dist3['range_min'] = 1.6
    dist1['range_max'] = 3
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
    dist3['c&dh_standard'] = True
    dist3['c&dh_optim'] = True
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
    dist4['c&dh_standard'] = True
    dist4['c&dh_optim'] = True
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
    dist5['c&dh_standard'] = True
    dist5['c&dh_optim'] = True
    dist5['struct_stand'] = True
    dist5['struct_high_resist'] = True

    bus_vs_dist.append(dist5)

    

    results['Status'] = 'Mission is possible'
    return StreamingHttpResponse(json.dumps(results), content_type="application/json") 

        



