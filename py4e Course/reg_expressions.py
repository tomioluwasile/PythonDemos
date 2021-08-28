# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:10:02 2020

@author: Tomi
"""
import re
import sys

def re_counter():
    '''user enters a RE, program counts number of lines
    matching the input'''
    count = 0
    fname = input('Enter a regular expression: ')
    fhand = open('mbox.txt')
    for line in fhand:
        line = line.rstrip()
        if re.search(fname, line):
            count += 1
    print('mbox.txt had', count, 'line(s) that matched', fname)

#re_counter()

def ave_new_revision():
    '''extract the numbers on the new revision line
    and compute the average'''
    count = 0
    nr_value = 0
    fname = input('Enter file name: ')
    try:
        fhand = open(fname)
    except FileNotFoundError:
        print(fname, 'does not exist')
        sys.exit()
    for line in fhand:
        line = line.rstrip()
        nr_line = re.findall('^New Rev.*: ([0-9.]+)', line)
        if len(nr_line) > 0:
            count += 1
            for value in nr_line:
                value = int(nr_line[0])
                nr_value += value
    average = nr_value / count
    print('Average New Revision value =', average)

#ave_new_revision()
