import json
from django.http import StreamingHttpResponse

# Create your views here.

def simulation(request):
    js = {'status': 'OK', 'response': 200}
    js = json.dumps(js)

    return StreamingHttpResponse(js, content_type="application/json")

