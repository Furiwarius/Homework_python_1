# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

import random

def quarter_definition(value):
    if value == 1: print("x>0; y>0")
    elif value == 2: print("x>0; y<0")
    elif value == 3: print("x<0; y<0")
    else:print("x<0; y>0")

value = random.randrange(1, 5)
print(f"номер четверти - {value}")
quarter_definition(value)