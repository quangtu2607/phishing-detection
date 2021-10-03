import requests
from lxml.html import fromstring

def get_proxies():
    url = 'https://free-proxy-list.net/'
    while True:
        try:
            response = requests.get(url, timeout=0.05)
            break
        except:
            continue
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr'):
        if i.xpath('.//td[7][contains(text(),"yes")]'):
        #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
            if len(proxies) == 5:
                break
    return proxies
