'''
Tests views
Need refactoring
'''
import json
from django.http import HttpResponse, StreamingHttpResponse
from models import Missions, Targets, Details, Planets, PayloadBusTypes, PayloadBusComps
from views import JSONResponse

def db(request):
    missions = Missions.objects.count()
    m_out = 'we follow '+str(missions)+' missions'

    details = Details.objects.count()
    d_out = 'we serve '+str(details)+' details about NASA, ESA, JAXA missions'
    
    

    out = {'missions': m_out, 'details': d_out }
    
    return JSONResponse(out)
