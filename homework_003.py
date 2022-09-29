# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

import random

def coordinate_generator():
    coordinate = []
    coordinate.append(random.randrange(-50, 50))
    coordinate.append(random.randrange(-50, 50))
    if coordinate[0]==0 or coordinate[1]==0: coordinate = coordinate_generator()
    return coordinate

def quarter_definition(xy):
    print(f"x = {xy[0]}; y = {xy[1]}")
    if xy[0] > 0 and xy[1] > 0: print(1)
    elif xy[0] > 0 and xy[1] < 0: print(2)
    elif xy[0] < 0 and xy[1] < 0: print(3)
    else: print(4)

coordinate = coordinate_generator()
quarter_definition(coordinate)