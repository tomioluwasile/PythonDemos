# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 15:19:48 2020

@author: Tomi
"""

def emailcount():
    fname = input('Enter file name: ')
    fhand = open(fname)
    count = 0
    for line in fhand:
        if line.startswith('From:'):
            count = count + 1
    print('There are', count, 'emails starting'
          ' with "From:" in the file', fname)
#emailcount()

def emailreceivecount():
    fname = input('Enter file name: ')
    fhand = open(fname)
    count = 0
    for line in fhand:
        if line.startswith('Received'):
            count = count + 1
    print('There are', count, 'emails received '
          'in the file', fname)
#emailreceivecount

def emailexercise2():
    try:
        fname = input('Enter file name: ')
    except:
        print('Please enter a valid file name')

    fhand = open(fname)
    prompt = input('Enter line to startwith: ')
    count = 0
    for line in fhand:
        if line.startswith(prompt):
            count = count + 1
            atpos = line.find(':')
            sppos = line.find('.', atpos)
            scvalue = float(line[atpos + 2 : sppos + 5])
            print(scvalue)
            total = 0
            for value in scvalue:
                total = total + value
            average = total / count
            print(average)

    print('There are', count, 'lines showing the '
          'spam confidence value. Average spam confidence'
          ' value is', average)
#emailexercise2
