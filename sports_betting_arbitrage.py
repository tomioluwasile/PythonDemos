# -*- coding: utf-8 -*-
'''
Created on Fri Jul 31 12:57:48 2020

@author: Tomi
'''

def arbitrage():
    '''Calculate profit to be made if you place two bets on two
    competing teams'''
    while True:
        try:
            odd1 = float(input('Enter selection 1 odds(e.g. 1.34): '))
            if 1 <= odd1 <= 500:
                break
        except (TypeError, ValueError):
            print('Please enter value between one and five hundred')
    while True:
        try:
            odd2 = float(input('Enter selection 2 odds(e.g. 4.60): '))
            if 1 <= odd2 <= 500:
                break
        except (TypeError, ValueError):
            print('Please enter value between one and five hundred')

    percent_arbi = ((1 / odd1) + (1 / odd2)) * 100
    print('Percentage arbitrage: ', percent_arbi)

    percent_profit = (100 - percent_arbi) / 100
    while True:
        try:
            stake = float(input('Enter stake amount: '))
            if 30 <= stake <= 4000000:
                break
        except (ValueError, TypeError):
            print('PLease enter value between 30 and 4,000,000')

    profit = int(stake * percent_profit)
    print('Your profit is ' + str(profit))
arbitrage() #review - print loss if there is a loss, instead of profit
