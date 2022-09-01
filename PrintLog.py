import imp
import time
import sys
import requests
from urllib.request import urlopen
import json

def pLog(str):
    timenow = time.strftime("%Y-%m-%d %H:%M:%S")
    print(timenow + "\t" + str)
    # writeArticleOnWeb(timenow, str)

def writeArticleOnWeb(title, contents):
    url = 'http://yuniverse.me/articles/write/'
    client = requests.session()

    while(True):
        try:
            client.get(url)  # sets cookie
        
        except:
            page = urlopen(url)
            doc = page.read().decode('utf-8')
            dic = json.loads(doc)
        
        else:
            if 'csrftoken' in client.cookies:
                # Django 1.6 and up
                csrftoken = client.cookies['csrftoken']
            else:
                # older versions
                csrftoken = client.cookies['csrf']

            write_url = 'http://yuniverse.me/articles/create/'
            data = dict(title=title, contents=contents, writer='UpbitAPI', board_name='Trading', csrfmiddlewaretoken=csrftoken, next='/')
            req = client.post(write_url, data=data, headers=dict(Referer=url))
            return req