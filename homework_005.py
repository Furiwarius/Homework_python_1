# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

import random, math

def coordinate_generator():
    coordinate = [] # [x1, y1, x2, y2]
    for i in range(4): coordinate.append(random.randrange(-50, 50))
    return coordinate

def finding_the_length(listXY):
    print(f"x1 = {listXY[0]}; y1 = {listXY[1]}")
    print(f"x2 = {listXY[2]}; y2 = {listXY[3]}")
    length = math.sqrt(pow(listXY[0] - listXY[2], 2) + pow(listXY[1] - listXY[3], 2))
    print(f"Расстояние между точками = {round(length, 3)}")


finding_the_length(coordinate_generator())