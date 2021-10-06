
from itertools import cycle
from urllib.parse import urlparse

from requests.api import head
import validate, proxyAPI, requests, random
url = 'https://medium.com/'
def clean():
    proxies = proxyAPI.get_proxies()
    proxy_pool = cycle(proxies)
    proxy = None
    timeout = False
    while True:
        if proxy == None:
            proxy = next(proxy_pool)
            print(proxy)
        try:
            if timeout:
                response = requests.get(url, proxies={'http': proxy, 'https': proxy})
            else:
                response = requests.get(url, timeout=0.05)
            if validate.isInActive(response.status_code):
                break
            if validate.isURL(url):
                domain = urlparse(url).netloc
                return domain
            timeout = False
            break
        except:
            proxy = next(proxy_pool)
            timeout = True
            continue

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
]
user_agent = random.choice(user_agents) 
headers = {'User-Agent': user_agent}       
proxy = '47.245.33.104:12345'
response = requests.get('amazon.com', allow_redirects=True, headers=headers)
print(response.content, response.url)