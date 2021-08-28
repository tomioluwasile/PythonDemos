# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:27:02 2020

@author: Tomi
"""

def palindrome():
    '''determine if a word can be spelt backward the same way
    it is spelt forward, e.g. racecar. Program terminates by entering
    break as input'''
    while True:
        try:
            prompt = str(input('Enter a string: '))
            prompt = prompt.lower().strip()
        except TypeError:
            print('Please enter a string')
        if prompt == 'do nothing':
            continue
        if prompt == 'break':
            break
        if prompt == prompt[::-1]:
            print(prompt, 'is a palindrome!')
        elif prompt != prompt[::-1]:
            print('Nope, try again')
palindrome()
