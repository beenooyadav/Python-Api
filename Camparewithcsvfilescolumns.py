# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 13:52:12 2017

@author: zemoso
"""
import json,codecs
import csv
import os.path

csvcolums={}
with codecs.open('csvcolums.txt', 'r', 'utf8') as f:
     csvcolums=json.load(f)
     
for table in csvcolums:
    csvfile = table+'.csv'
    if os.path.isfile(csvfile):
        with open(csvfile, 'r') as f:
          reader = csv.reader(f)
          
          columns1=table+'1'
          columns2=table+'2'
          columnsmissing=table+'missing'
          
          columns1= list(reader)[0]
          columns2= csvcolums[table]
          columnsmissing=[]
          for column in columns2:
              if column not in columns1:
                  columnsmissing.append(column)
          print csvfile
          print columnsmissing
