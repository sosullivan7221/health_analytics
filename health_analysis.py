import pandas as pd
import numpy as np


favorite_number = 4
favorite_color = 'green'
days_of_the_week = ['Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday']
patient = {'ID': 14673317, 'Name': {'First Name': 'Sean', 'Last Name': 'OSullivan'}, 'Allergies': ['Pollen', 'Peanuts']}


print(favorite_number)
print(favorite_color)
print(days_of_the_week)
print(patient)


def drink_legally(name, age):
    if age < 21:
        results = name + ' cannot legally drink.'
    else:
        results = name + ' can legally drink.'
    return results

legal_drink_result = drink_legally('Sean', 21)

print('Can this person drink?: ' + legal_drink_result)




        