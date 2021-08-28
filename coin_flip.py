# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 13:10:08 2020

@author: Tomi
"""

import random # for computer-generated random selections

def coin_flip():
    '''simulate the flipping of a coin, record the outcomes
    and count the number of tails and heads'''
    while True:
        try:
            flip_times = int(input('Enter no of flips: '))
            break
        except (TypeError, ValueError):
            print('Please enter a valid integer')
    count = 0
    heads = 0
    tails = 0
    while flip_times > count:
        rand = random.randint(1, 2)
        #print('Debug:', rand)
        if rand == 1:
            flip = 'head'
            heads += 1
        elif rand == 2:
            flip = 'tail'
            tails += 1
        print('flip ' + str(count) + ': ' + str(flip))
        count += 1
    print('Total number of flips: ' + str(count))
    print('Total number of heads: ' + str(heads))
    print('Total number of tails: ' + str(tails))
coin_flip()
