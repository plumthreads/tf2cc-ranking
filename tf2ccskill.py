# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 23:21:55 2022

@author: Tony
"""

from loginput import *
from openskill import Rating, rate

urls = clean_data('tf2cc_logs.csv')
logresults = log_to_res(urls)

players = {}

for res in logresults:
    #create default ratings if not in players dict
    for redplayer in res[0]:
        if redplayer not in players:
            players[redplayer] = Rating()
    for bluplayer in res[1]:
        if bluplayer not in players:
            players[bluplayer] = Rating()
    #update ratings with result
    reds = []
    blus = []
    for p in res[0]:
        reds.append(players[p])
    for p in res[1]:
        blus.append(players[p])
    [reds,blus] = rate([reds, blus], score = res[2])
    for c,p in enumerate(res[0]):
        players[p] = reds[c]
    for c,p in enumerate(res[1]):
        players[p] = blus[c]
    
    