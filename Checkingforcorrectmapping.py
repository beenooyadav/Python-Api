# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 14:00:06 2017

@author: zemoso
"""
import json,codecs
from openpyxl import load_workbook

aifmapping={}
with codecs.open('aifmapping.txt', 'r', 'utf8') as f:
     aifmapping=json.load(f)

workbook = load_workbook('Data Mapping Document 170927.xlsx', use_iterators=True)
first_sheet = workbook.get_sheet_names()[0]
worksheet = workbook.get_sheet_by_name(first_sheet)