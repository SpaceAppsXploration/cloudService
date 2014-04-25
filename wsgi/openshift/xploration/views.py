import json
from django.http import StreamingHttpResponse
import random
from django.shortcuts import render_to_response
from django.http import Http404
import datetime

# import verity tables for mission's checking
from data.tables_Bodies import destinations
from data.tables_Missions import mission_type
from data.tables_BusVsMission import bus_vs_mission_type
from data.tables_BusVsDist import bus_vs_dist
from data.tables_BusVsBus import bus_vs_bus
from data.missions import missions
from data.missions_details import missions_details

from models import Missions, Targets, Details

def home(request):
    js = {'status': 'Coming Soon...', 'response': 200, 'code': 0}
    js = json.dumps(js)
    
    params = {}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'
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

    # Script creazione record in Details (ca. 1400)
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

        



