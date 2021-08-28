# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:15:28 2020

@author: Tomi
"""

import math # for numerical calculations

def mortgage_calculator():
    '''mortgage calculator from Mosh's Java course
    (my python version)'''
    percent = 100
    mon_in_a_year = 12

    while True:
        try:
            annual_rate = float(input("Enter annual rate: \n"))
            if 1 <= annual_rate <= 30:
                break
            print('Please enter a rate between 1% and 30%')
        except (TypeError, ZeroDivisionError, ValueError):
            print('Please enter a valid number')
    while True:
        try:
            principal = float(input("Enter amount: \n"))
            if 1000 <= principal <= 1000000:
                break
            print('Please enter a principal between 1,000 and 1,000,000')
        except (TypeError, ZeroDivisionError, ValueError):
            print('Please enter a valid number')
    while True:
        try:
            years = float(input("Enter number of years: \n"))
            if 1 <= years <= 50:
                break
            print('Please enter a period between one and fifty years')
        except (TypeError, ZeroDivisionError, ValueError):
            print('Please enter a valid number')

    no_of_payments = years * mon_in_a_year
    monthly_rate = annual_rate / percent / mon_in_a_year

    mortgage = (principal
                * (monthly_rate * math.pow((1 + monthly_rate), no_of_payments))
                / (math.pow((1 + monthly_rate), no_of_payments) - 1))

    print("Mortgage (per month): ", mortgage)
mortgage_calculator()
