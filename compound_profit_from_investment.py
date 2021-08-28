# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:15:28 2020

@author: Tomi
"""

def compound_profit():
    '''calculate your compound profit from an investment of x over a 
    period of y months at a rate of z. x is reinvested monthly'''
    while True:
        try:
            principal = int(input('Enter principal amount: '))
            if principal >= 50000:
                break
            print('Please enter an amount greater than N50,000')
        except (TypeError, ValueError):
            print('Error. Enter a numerical value instead')
    while True:
        try:
            prompt = int(input('Enter percentage rate (e.g. 25): '))
            if 1 <= prompt <= 50:
                break
            print('Please enter a rate between 1% and 50%')
        except (TypeError, ValueError):
            print('Error. Enter a numerical value instead')

    while True:
        try:
            # this should be adjusted to account for period in days
            # like 25 days type of ROIs
            period = int(input('Enter period in months: '))
            if period >= 1:
                break
            print('Please ensure period is at least a month')
        except (TypeError, ValueError):
            print('Error. Enter a numerical value insted')

    # there should be a better way to write this in different
    # functions, probably a class thing. But let's work with
    # what we have here anyway
    rate = prompt/100

    new_principal = principal
    i = 0
    while i < period:
        i += 1
        profit = new_principal * rate
        new_principal += profit
        print('Month ' + str(i) + ' : N' + str(new_principal))
        #print('Debug: Final amount -', 'N' + str(new_principal))
    final_profit = new_principal - principal
    print('\n  Your profit after', period, 'months of investment',
          'at the rate of', prompt, '% per month is N', final_profit)
    print('\n  Total amount with compound interest is N', new_principal)
compound_profit()
