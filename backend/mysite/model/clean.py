from datetime import time
from itertools import cycle
import pandas as pd
import validate, proxyAPI, os, requests, random
from urllib.parse import urlparse
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
par_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
path = os.path.relpath('..\\data\\sample.csv', par_path)
testPath = os.path.relpath('..\\data\\test.csv', par_path)
df = pd.read_csv(path, encoding = "ISO-8859-1", usecols=['url', 'domain'])
df = df.astype({'url': str, 'domain': str})

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
]

def clean():
    proxies = proxyAPI.get_proxies()
    proxy_pool = cycle(proxies)
    proxy = None
    timeout = False
    s = requests.Session()
    retries = Retry(total=3, raise_on_redirect=True)
    user_agent = random.choice(user_agents) 
    headers = {'User-Agent': user_agent}
    s.mount('', HTTPAdapter(max_retries=retries))
    for index, data in df.iterrows():
        url = data['url'] if not pd.isnull(df.loc[index, 'url']) else data['domain']
        count = 0
        if validate.isIP(url) or not (validate.isURL(url) or validate.isDomain(url)):
            df.drop(index=index, inplace=True)
        while True:
            try:
                if validate.isDomain(url):
                    df.at[index, 'url'] = 'https://' + url
                    if validate.isDomainActive(url):
                        df.at[index, 'state'] = 'ACTIVE'
                    else:
                        df.at[index, 'state'] = 'INACTIVE'
                    break
                if timeout:
                    response = s.get(url, proxies={'http': proxy, 'https': proxy}, allow_redirects=True, headers=headers)
                else:
                    response = s.get(url, allow_redirects=True, headers=headers)
                url = response.url
                if validate.isInActive(response.status_code):
                    df.at[index, 'state'] = 'INACTIVE'
                else:
                    df.at[index, 'state'] = 'ACTIVE'
                domain = urlparse(url).netloc
                df.at[index, 'domain'] = domain
                timeout = False
                break
            except Exception as e:
                print(e)
                proxy = next(proxy_pool)
                timeout = True
                count += 1
                continue
            finally:
                if count == 6:
                    df.drop(index=index, inplace=True)
                    timeout = False
                    break
        if index == 0:
            df[:10].to_csv('data/test.csv')
            print(e)