# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 21:06:38 2022

@author: Tony
"""

import csv, urllib.request, json


def read_csv(filename):
    with open(filename, 'r', encoding="utf8") as f:
        lines = csv.reader(f,delimiter=',')
        return list(lines)[1:] #remove header row
    
def clean_data(filename):
    data = read_csv(filename)
    data = list(filter(lambda x: x[1]=='Machu the Robot 2#0767',data))
    return list(map(lambda x:x[3], data))

def match_parser(match_data):
    #takes python dict
    #returns match result
    scores = []
    redplayers = []
    bluplayers = []
    scores.append(match_data['teams']['Red']['score'])
    scores.append(match_data['teams']['Blue']['score'])
    for player in match_data['players']:
        if match_data['players'][player]['team'] == 'Red':
            redplayers.append(player)
        elif match_data['players'][player]['team'] == 'Blue':
            bluplayers.append(player)  
    return [redplayers,bluplayers,scores]
    
def log_to_res(urls):
    link_ids = []
    results = []
    for link in urls:
        link_ids.append(link[-7:]) #assumes 7 char id 
    for link_id in link_ids:
        with urllib.request.urlopen("http://logs.tf/json/"+link_id) as url:
            match_data = json.loads(url.read().decode())
            results.append(match_parser(match_data))
    return results
            
            