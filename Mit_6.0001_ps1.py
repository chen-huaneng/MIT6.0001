# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:05:15 2023

@author: Abel
"""
#ps1-a
annual_salary = float(input('Enter your annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost = float(input('Enetr the cost of your dream home:'))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
month = 0

monthly_salary = annual_salary / 12
monthly_saving = monthly_salary * portion_saved
down_payment = portion_down_payment * total_cost

while current_savings < down_payment:
    current_savings += current_savings * r / 12
    current_savings += monthly_saving
    month += 1
    
print('Number of months:',month)
#ps1-b
annual_salary = float(input('Enter your annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost = float(input('Enetr the cost of your dream home:'))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal:'))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
month = 0

monthly_salary = annual_salary / 12
monthly_saving = monthly_salary * portion_saved
down_payment = portion_down_payment * total_cost

while current_savings < down_payment:
    if month%6 == 0 and month != 0:
        monthly_salary += monthly_salary * semi_annual_raise
        monthly_saving = monthly_salary * portion_saved
        
    current_savings += current_savings * r / 12
    current_savings += monthly_saving
    month += 1
    
print('Number of months:',month)
#ps1-c
annual_salary = float(input('Enter your annual salary:'))

total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
r = 0.04
step = 0
low = 0
high = 10000
month = 0
ans = (low + high) / 2
down_payment = portion_down_payment * total_cost

while True:
    ans = (low + high) / 2
    current_savings = 0
    portion_saved = ans / 10000
    monthly_salary = annual_salary / 12
    monthly_saving = monthly_salary * portion_saved
    month = 0
    for x in range(36):
        if month % 6 == 0 and month != 0:
            monthly_salary += monthly_salary * semi_annual_raise
            monthly_saving = monthly_salary * portion_saved
        current_savings += current_savings * r / 12
        current_savings += monthly_saving
        month += 1
        
    step += 1
    if low == high:
        print('It is not possible to pay the down payment in three years.')
        break
    if abs(current_savings - down_payment) <= 100:
        print('Best savings rate:','%.4f'%portion_saved)
        print('Steps in bisection search:',step)
        break
    elif down_payment > current_savings - 100:
        low = ans
    elif down_payment <= current_savings - 100:
        high = ans