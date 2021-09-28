from django.shortcuts import render

# Create your views here.
import json
from django.contrib.auth.models import User #####
from django.http import JsonResponse , HttpResponse ####
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Hello, world")

@csrf_exempt
def get_page(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        print(body_data['content'])
        print(body_data['url'])
    # Any process that you want
    data = {
            # Data that you want to send to javascript functions
    }
    return HttpResponse("Your response")