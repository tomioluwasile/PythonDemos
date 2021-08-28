# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 19:54:04 2020

@author: Tomi
This contains solutions to some list exercises from the 
Python for Everybody (py4e) Course
"""
import sys

def max_and_min():
    '''prompt user for numbers and compute max and min'''
    number_list = []
    while True:
        prompt = input('Enter number: ')
        try:
            value = float(prompt)
            number_list.append(value)
        except (TypeError, ZeroDivisionError, ValueError):
            if prompt == 'done' or prompt == 'Done':
                break
            else:
                print('enter a numerical value')
    maximum = max(number_list)
    minimum = min(number_list)
    print('Max:', maximum, 'Min:', minimum)
#max_and_min()

def confidence_value():
    '''compute average c value'''
    fname = input('Enter file name: ')
    try:
        fhand = open(fname)
    except FileNotFoundError:
        if fname == 'na na boo boo':
            print("NA NA BOO BOO TO YOU - "
                  "You've been punk'd!")
        else:
            print('File does not exist')
        sys.exit()
    count = 0
    confidencesum = 0
    for line in fhand:
        if line.startswith('X-DSPAM-Confidence:'):
            count += 1
            words = line.split()
            confidence = float(words[1])
            confidencesum += confidence
    try:
        average = confidencesum / count
        print('The average confidence value is', average)
    except ZeroDivisionError:
        print('0 lines exist in the form requested')
#confidence_value()

def a_message_from():
    '''find who sent the email'''
    count = 0
    fname = input('Enter file name: ')
    try:
        fhand = open(fname)
    except FileNotFoundError:
        print(fname, 'does not exist')
        exit()
    for line in fhand:
        line = line.rstrip()
        words = line.split()
        if len(words) == 0:
            continue
        if words[0] == 'From':
            count += 1
            print(words[1])
    print('There were', count, 'lines in the file '
          'with From as the first word')

#a_message_from()

def my_romeo():
    '''parsing romeo.txt file'''
    words = []
    myset = set()
    with open('romeo.txt') as fhand:
        for line in fhand:
            line = line.rstrip()
            for word in line.split():
                #print(word)
                if word not in words:
                    words.append(word)
                    myset.add(word)
                    words.sort()
        print(words)
        #print(myset)
#my_romeo()
