# -*- coding: utf-8 -*-
'''
Created on Fri Jul 31 12:57:48 2020

@author: Tomi
'''

import random # for random number selection

def the_random_game():
    '''user guesses a random number from 1 to 100, program terminates 
    when the user gives the same answer as the computer'''
    name = input('Hey there! What\'s your name? \n')
    print('Welcome ' + name + '. ' 'Let\'s play a game.')
    print('I\'m thinking of a number from 1 to 100, '
          'Can you guess?')
    answer = random.randint(1, 100)
    count = 1
    while True:
        try:
            prompt = input('Enter guess: ')
            userguess = int(prompt)
            if userguess < answer:
                print('Your guess was too low, '
                      'another try?')
            elif userguess > answer:
                print('Your guess was too high, '
                      'another try?')
            elif userguess == answer:
                break
            for unused_attempt in prompt:
                count += 1
        except (NameError, TypeError):
            print('That didn\'t work. '
                  'Enter a numerical value')
    print('You guessed the right answer in', count,
          'guesses. The answer is ' + str(answer))
the_random_game() 
# give user only 5 attempts
# debug count error
