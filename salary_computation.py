# -*- coding: utf-8 -*-
'''
Created on Fri Jul 31 12:57:48 2020

@author: Tomi
'''

def compute_pay(_hour_, _rate_):
    '''salary computation based on hourly rate, number of hours worked
    and bonus in overtime pay'''
    hours = float(_hour_)
    rate = float(_rate_)
    try:
        if hours <= 40:
            pay = hours * rate
            return pay
        if hours > 40: #bonus for overtime
            overtime = float((hours - 40) * (1.5 * rate))
            pay = (40 * rate) + overtime
            return pay
    except (NameError, TypeError):
        print('Please enter a numerical value')
    return pay
compute_pay(45, 20) 
# modify for other input methods
