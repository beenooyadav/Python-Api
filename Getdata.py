# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:13:33 2017

@author: zemoso
"""

import requests
import codecs, json
  
request={
    'Accept' :'application/json, text/plain, */*',
    'Accept-Encoding' :'gzip, deflate, br',
    'Accept-Language' :'en-GB,en-US;q=0.8,en;q=0.6',
    'Authorization': 'Bearer 78f42c6e-274e-4ffc-93eb-33f0e03e715f',
    'Connection' :'keep-alive',
    'Host' :'cs-configapi.agilone.com',
    'Origin' :'https://cs-config.agilone.com',
    'Referer' :'https://cs-config.agilone.com/connector/list',
    'User-Agent' :'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
r = requests.get('https://cs-configapi.agilone.com/v2/83/config/connectors?limit=500&offset=0', headers=request)
  
print r.status_code
jsonobject= r.json()
mappings= [i['mapping'] for i in jsonobject['content'] if 'mapping' in i]

with codecs.open('data.txt', 'w', 'utf8') as f:
     f.write(json.dumps(mappings[0],indent=3, ensure_ascii=False))