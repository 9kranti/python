"""
15. Find area of circle
"""
import math


def area_of_circle():

    radius = int(input("Enter the value for radius: "))

    area_of_circle = math.pi * radius * radius
    print("Area of circle is",area_of_circle)

area_of_circle()