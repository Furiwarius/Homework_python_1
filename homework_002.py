# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
import random

X=random.randrange(0,2)
Y=random.randrange(0,2)
Z=random.randrange(0,2)
print(f"X = {X}")
print(f"Y = {Y}")
print(f"Z = {Z}")

left_side = not (X+Y+Z)
right_side = (not X) * (not Y) * (not Z)

if left_side == right_side: print(True)
else: print(False)