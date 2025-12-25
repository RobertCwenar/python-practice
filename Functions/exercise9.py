#Create the program which ask the user to calculate the area of the selected figure:
# 1) Rectangle
# 2) Square
# 3) Triangle
# 4) Trapezoid
# 5) Circle

import math

while True:
    print("Choose the figure to calculate the area: ")
    print("1) Rectangle")
    print("2) Square")
    print("3) Triangle")
    print("4) Trapezoid")
    print("5) Circle")
    print("6) Exit")


    
    choice = input("Enter your choice (1-6) or write name of the figure: ")
    
    if choice == "1" or choice.lower() == "rectangle":
        def area_of_rectangle(length, width):
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            return length * width

        print(f"The area of the rectangle is: {area_of_rectangle(0,0)}")
    
    cont = input(f" Do you want to continue? (yes/no):").lower()
    if cont == 'no':
        print("Exiting the program.")
        break

    if choice == "2" or choice.lower() == "square":
        def area_of_square(side):
            side = float(input("Enter the side of the square: "))
            return side * side

        print(f"The area of the square is: {area_of_square(0)}")

    cont = input(f" Do you want to continue? (yes/no):").lower()
    if cont == 'no':
        print("Exiting the program.")
        break

    if choice == "3" or choice.lower() == "triangle":
        def area_of_triangle(base, height):
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            return 0.5 * base * height
        print(f"The area of the triangle is: {area_of_triangle(0,0)}")

    cont = input(f" Do you want to continue? (yes/no):").lower()
    if cont == 'no':
        print("Exiting the program.")
        break

    if choice == "4" or choice.lower() == "trapezoid":
        def area_of_trapezoid(base1, base2, height):
            base1 = float(input("Enter the first base of the trapezoid: "))
            base2 = float(input("Enter the second base of the trapezoid: "))
            height = float(input("Enter the height of the trapezoid: "))
            return 0.5 * (base1 + base2) * height
        
        print(f"The area of the trapezoid is: {area_of_trapezoid(0,0,0)}")

    cont = input(f" Do you want to continue? (yes/no):").lower()
    if cont == 'no':
        print("Exiting the program.")
        break

    if choice == "5" or choice.lower() == "circle":
        def area_of_circle(radius):
            radius = float(input("Enter the radius of the circle: "))
            return math.pi * radius * radius

        print(f"The area of the circle is: {area_of_circle(0)}")

    cont = input(f" Do you want to continue? (yes/no):").lower()
    if cont == 'no':
        print("Exiting the program.")
        break

    if choice == "6" or choice.lower() == "exit":
        print("Exiting the program.")
        break