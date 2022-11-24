# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
import math
x1 = float(input("x = "))
y1 = float(input("y = "))
x2 = float(input("x = "))
y2 = float(input("y = "))
ab = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(round(ab,2)) 