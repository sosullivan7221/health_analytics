import pandas as pd
import numpy as np


favorite_number = 4
favorite_color = 'green'
days_of_the_week = ['Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday']
first_six_months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6}

print(favorite_number)
print(favorite_color)
print(days_of_the_week)
print(first_six_months)


def drink_legally(name, age):
    if age < 21:
        results = name + ' cannot legally drink.'
    else:
        results = name + ' can legally drink.'
    return results

legal_drink_result = drink_legally('Sean', 21)

print('Can this person drink?: ' + legal_drink_result)




        