# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:27:02 2020

@author: Tomi
"""

import random # for random number selection

def lotto():
    '''ask user for 6 numbers in certain range. Program then displays
    6 random numbers from the same range, and check the numbers the
    user guessed correctly'''

    input_lst = []
    computer_lst = []
    count = 0
    while True:
        try:
            prompt = int(input('Enter an int between 1-49 (6 tries): '))
            if prompt not in range(1, 49):
                print('Value not in desired range')
            input_lst.append(prompt)
            if len(input_lst) == 6:
                break
        except (TypeError, ValueError):
            print('Please enter a list of 6 integers from 1 - 49')
    print('Your guesses: ', input_lst)
    for i in range(6):
        generate = random.randint(1, 49)
        computer_lst.append(generate)
    print('Lotto system: ', computer_lst)
    for value in input_lst:
        if value in computer_lst:
            count += 1
    print('Total number of correct predictions:', count)
lotto()
