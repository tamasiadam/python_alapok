"""
import random
random_szam = random.randint(1, 3)

szam = int(input("Adj meg egy egész sámot 1 és 3 között! "))
if szam == random_szam:
    print("Ez a szám egyezik!")
else:
    print("A szám sajnos NEM egyezik.")
print(random_szam)


import random
"""

import random

random_dobas = random.randint(1, 2)

valasz = input("Fej vagy írás?\nVálaszod: ")

if random_dobas == 1:
    print("Fej")
if random_dobas == 2:
    print("Írás")
if random_dobas == valasz:
    print("Eltaláltad!")
else:
    print("Vesztettél!")
