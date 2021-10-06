from django.shortcuts import render

# Create your views here.
import json
from django.contrib.auth.models import User #####
from django.http import JsonResponse , HttpResponse ####
from django.views.decorators.csrf import csrf_exempt
import whois
from itertools import cycle
from urllib.parse import urlparse
from phishing import validate, proxyAPI
import requests, random


def index(request):
    return HttpResponse("Hello, world")

@csrf_exempt
def get_pageinfo(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        # print(body_data['content'])
        # print(body_data['url'])

        # w = whois.whois(body_data['url'])
        # print(w)

    # Any process that you want
    url = body_data['url']

    user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
    ]

    user_agent = random.choice(user_agents) 
    headers = {'User-Agent': user_agent}       
    response = requests.get(url, allow_redirects=True, headers=headers)
    print(response.content, response.url)

    data = {
            # Data that you want to send to javascript functions
    }
    return HttpResponse("Your response")