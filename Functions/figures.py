import math

def area_of_square(side):
    return side * side

def area_of_rectangle(length, width):
    return length * width

def area_of_circle(radius):
    return math.pi * radius * radius

def area_of_triangle(base, height):
    return 0.5 * base * height  

def area_of_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height