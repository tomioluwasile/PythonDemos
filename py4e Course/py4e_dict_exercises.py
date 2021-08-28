# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 13:44:48 2020

@author: Tomi

This contains solutions to some dictionary exercises from the 
Python for Everybody (py4e) Course
"""

import sys
import string


def exe2():
    '''exercise 2: count days of the week'''
    counts_dict = {}
    fname = input('Enter file name: ')
    try:
        fhand = open(fname)
    except FileNotFoundError:
        print(fname, 'does not exist')
        sys.exit()
    for line in fhand:
        line.rstrip()
        words = line.split()
        for word in words:
            if len(word) == 0:
                continue
            if words[0] != 'From':
                continue
            days = words[2]
            #print('debug: ', days)
            days = days.split()
            for day in days:
                counts_dict[day] = counts_dict.get(day, 0) + 1
    print(counts_dict)
    #day with the highest number of emails received
    maximum = 0
    max_key = None
    for key in counts_dict:
        if counts_dict[key] > maximum:
            maximum = counts_dict[key]
            max_key = key
    print('Number of emails:', maximum, '\n'
          'Day of the week:', max_key)

#exe2()

def exe3():
    '''counts no of messages from each email address'''
    counts_dict = {}
    fname = input('Enter file name: ')
    try:
        fhand = open(fname)
    except FileNotFoundError:
        print(fname, 'does not exist')
        sys.exit()
    for line in fhand:
        line.rstrip()
        words = line.split()
        for word in words:
            if len(word) == 0:
                continue
            if words[0] != 'From':
                continue
            emails = words[1]
            #print('Debug: ', emails)
            emails = emails.split()
            for email in emails:
                counts_dict[email] = counts_dict.get(email, 0) + 1
    print(counts_dict)
    # exercise 4 - maximum and minimum loop
    #email with highest number of messages received from
    maximum = 0
    max_key = None
    for key in counts_dict:
        if counts_dict[key] > maximum:
            maximum = counts_dict[key]
            max_key = key
    print('Email address:', max_key, '\n'
          'Number of emails:', maximum)

#exe3()

def exe5():
    '''print domain name instead of full email address'''
    counts_dict = {}
    fname = input('Enter file name: ')
    try:
        fhand = open(fname)
    except FileNotFoundError:
        print(fname, 'does not exist')
        sys.exit()
    for line in fhand:
        line.rstrip()
        if not line.startswith('From'):
            continue
        atpos = line.find('@')
        sppos = line.find(' ', atpos)
        domain_name = line[atpos + 1 : sppos]
        #print(domain_name)
        domain_name = domain_name.split()
        for domain in domain_name:
            counts_dict[domain] = counts_dict.get(domain, 0) + 1
    print(counts_dict)
    #to arrange in alphabeticsl order (optional)
    lst = list(counts_dict.keys())
    lst.sort()
    for key in lst:
        print(key, counts_dict[key])

#exe5()

def exe1_tupledict():
    '''tuple and dictionary combined
    More like complex data structures'''
    email_dict = {}
    count = 0
    fname = input('Enter file name: ')
    try:
        fhand = open(fname)
    except FileNotFoundError:
        print(fname, 'does not exist')
        sys.exit()
    for line in fhand:
        count += 1
        line.rstrip()
        words = line.split()
        for word in words:
            if len(word) == 0:
                continue
            if words[0] != 'From':
                continue
            emails = words[1]
            emails = emails.split()
            for email in emails:
                email_dict[email] = email_dict.get(email, 0) + 1
    lst = []
    for key, value in email_dict.items():
        lst.append((value, key))
    lst.sort(reverse=True)
    print('Number of lines in the file:', count)
    for key, value in (lst[:3]):
        print(key, value)

#exe1_tupledict()

def exe2_tupledict():
    '''time of day'''
    time_dict = {}
    fname = input('Enter file name: ')
    try:
        fhand = open(fname)
    except FileNotFoundError:
        print(fname, 'does not exist')
        sys.exit()
    for line in fhand:
        line.rstrip()
        words = line.split()
        for word in words:
            if len(word) == 0:
                continue
            if words[0] != 'From':
                continue
            time = words[5]
            #print(time)
            hour, minute, second = time.split(':')
            hour = hour.split()
            for needed_hour in hour:
                time_dict[needed_hour] = time_dict.get(needed_hour, 0) + 1
    lst = []
    for key, value in time_dict.items():
        lst.append((key, value))
    lst.sort()
    for key, value in lst:
        print(key, value)

#exe2_tupledict()

def exe3_tupledict():
    '''letters in decreasing order of frequency'''
    counts_dict = {}
    fname = input('Enter file name: ')
    try:
        fhand = open(fname)
    except FileNotFoundError:
        print(fname, 'does not exist')
        sys.exit()
    for line in fhand:
        line.rstrip()
        #remove spaces and characters
        line.translate(line.maketrans('', '', string.punctuation))
        line.lower()
        words = line.split()
        for word in words:
            counts_dict[word] = counts_dict.get(word, 0) + 1
    lst = []
    for key, value in counts_dict.items():
        lst.append((value, key))
    lst.sort(reverse=True)
    for key, value in lst:
        print(key, value)

#exe3_tupledict()
