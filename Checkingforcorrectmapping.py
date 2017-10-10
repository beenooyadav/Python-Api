# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 14:00:06 2017

@author: zemoso
"""
import json,codecs
import xlrd

aifmapping={}
with codecs.open('aifmapping.txt', 'r', 'utf8') as f:
     aifmapping=json.load(f)

workbook = xlrd.open_workbook('Data Mapping Document 170927.xlsx')
sheets = workbook.sheet_names()

missingattribute={}# attributes that are in aif but not in DM
mappingerror={}# mappings wrong in aif
missingtable={} #tables missing in DM

for sheet in sheets:
    if sheet.lower() in aifmapping:
        worksheet = workbook.sheet_by_name(sheet)
        #a dictionary for row number of attributes
        attributes={}        
        for row in range(5,worksheet.nrows):
            attribu=str(worksheet.cell(row,0))[7:-1].strip()
            attributes[attribu]=row
        #a dictionary to have column number of a csvfile
        csvtables={}
        for col in range(worksheet.ncols):
            table=str(worksheet.cell(1,col)).split('_',1)[0][7:]
            if table.lower() in aifmapping:
                if table not in csvtables:
                    csvtables[table] = col
        
        for attribute in aifmapping[sheet.lower()]:
            tabl= aifmapping[sheet.lower()][attribute]['table']
            colum= aifmapping[sheet.lower()][attribute]['column']
            flag=0
            
            #attribute checking
            if attribute not in attributes:
                if sheet in missingattribute:
                    missingattribute[sheet].append(attribute)
                else:
                    missingattribute[sheet]=[attribute]
                flag=1
            #table checking
            if tabl not in csvtables:
                if sheet in missingtable:
                    missingtable[sheet].append(tabl)
                else:
                    missingtable[sheet]=[tabl]
                flag=1
                
            if flag==0 and str(worksheet.cell(attributes[attribute],csvtables[tabl]))[7:-1] != colum:
                if sheet in mappingerror:
                    mappingerror[sheet].append(aifmapping[sheet.lower()][attribute])
                else:
                    mappingerror[sheet]=[aifmapping[sheet.lower()][attribute]]
with codecs.open('missingattribute.txt', 'w', 'utf8') as f:
     f.write(json.dumps(missingattribute,indent=3, ensure_ascii=False))

with codecs.open('mappingerror.txt', 'w', 'utf8') as f:
     f.write(json.dumps(mappingerror,indent=3, ensure_ascii=False))

with codecs.open('missingtable.txt', 'w', 'utf8') as f:
     f.write(json.dumps(missingtable,indent=3, ensure_ascii=False))