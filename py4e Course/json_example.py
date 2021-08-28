# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:15:28 2020

@author: Tomi
"""

import json

def get_started_with_json():
    '''this is how json looks like'''
    data = '''
    [
     { "Id" : "002", "Name" : "Bartowski", "Age" : "3"
     },
     { "Id" : "005", "Name" : "Simon", "Age" : "3"
     }
    ]'''

    info = json.loads(data)
    print('User Count:', len(info))

    for item in info:
        print('Name:', item['Name'])
        print('Id:', item['Id'])
        print('Attribute:', item['Age'])
get_started_with_json()
