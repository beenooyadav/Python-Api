# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 18:03:23 2017

@author: zemoso
"""
import json,codecs

data={}
with codecs.open('data.txt', 'r', 'utf8') as f:
     data=json.load(f)

aifmapping={}
csvcolums={}
for m in data:
    if m[0]['table'] in csvcolums:
        csvcolums[m[0]['table']].append(m[0]['column'])
    else :
        csvcolums[m[0]['table']]=[m[0]['column']]
    for v in m[1]:
        if v['table'] in aifmapping:
            aifmapping[v['table']][v['column']]=m[0]
        else :
            aifmapping[v['table']]={}
            aifmapping[v['table']][v['column']]=m[0]

with codecs.open('aifmapping.txt', 'w', 'utf8') as f:
     f.write(json.dumps(aifmapping,indent=3, ensure_ascii=False))
     
with codecs.open('csvcolums.txt', 'w', 'utf8') as f:
     f.write(json.dumps(csvcolums,indent=3, ensure_ascii=False))
