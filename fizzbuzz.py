# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:15:28 2020

@author: Tomi
"""

def fizzbuzz():
    '''another exercise from Java course
    print fizz if number is divisible by 5
    print buzz if number is divisible by 3
    print fizzbuzz if number is divisible by both 5 and 3'''

    while True:
        try:
            query = int(input('Enter number: '))
            if query > 0:
                break
        except (TypeError, ValueError):
            print('Please enter a valid number')
    # defining the conditions
    if (query % 5 == 0) and (query % 3 == 0):
        print('fizzbuzz')
    elif query % 5 == 0:
        print('fizz')
    elif query % 3 == 0:
        print('buzz')
    else:
        print(query, 'is neither divisible by 5 nor 3')
fizzbuzz()
