from django.shortcuts import render_to_response
import json
from django.template import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.context_processors import csrf
from django.core.mail import EmailMessage

def home(request):
    js = {'status': 'Coming Soon...', 'response': 200, 'code': 0, 'type': 'null', 'content': 'null'}
    js = json.dumps(js)
    
    params = {}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'
    params['status'] = js
    return render_to_response('home/home.html', params, context_instance=RequestContext(request))

def about(request):
    js = {'status': 'Coming Soon...', 'response': 200, 'code': 0, 'type': 'null', 'content': 'null'}
    js = json.dumps(js)
    
    params = {}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'
    params['status'] = js
    return render_to_response('home/about.html', params, context_instance=RequestContext(request))

def promo(request):
    js = {'status': 'Coming Soon...', 'response': 200, 'code': 0, 'type': 'null', 'content': 'null'}
    js = json.dumps(js)
    
    params = {}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'
    params['status'] = js
    return render_to_response('home/promo.html', params, context_instance=RequestContext(request))


@ensure_csrf_cookie
def wphoneregister(request):
    if request.method == 'GET':
        params = {}

        return render_to_response('home/wphonebeta.html', params,
                              context_instance=RequestContext(request))


    if request.method == 'POST':
        subscriber = request.POST['subscriber']

        to = ["dev.xploration@outlook.com"]
        sender = "Chronos Project <chronosprojectserver@gmail.com>"
        subject = "BETA ENROLLMENT REQUEST"
        content_txt = '''Somebody asked to enroll: \n
                       Email: '''+subscriber+'''\n
                       '''
        message = EmailMessage(subject, content_txt, from_email=sender, to=to)
            
        message.send()

        msg = {'message': 'Thanks for enrolling, you will receive an email with further instructions from our developers soon.'}
        return render_to_response('home/wphonebeta.html', msg,
                              context_instance=RequestContext(request))
