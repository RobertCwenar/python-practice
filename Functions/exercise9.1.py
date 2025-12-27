#Create the program which ask the user to calculate the area of the selected figure:
# 1) Rectangle
# 2) Square
# 3) Triangle
# 4) Trapezoid
# 5) Circle

import math

def area_of_rectangle(length, width):
    return length * width

def area_of_square(side):
    return side * side

def area_of_triangle(base, height):
    return 0.5 * base * height

def area_of_trapezoid(base1, base2, height):    
    return 0.5 * (base1 + base2) * height

def area_of_circle(radius):
    return math.pi * radius * radius

while True:
    print("\nChoose the figure to calculate the area: ")
    print("1) Rectangle")
    print("2) Square")
    print("3) Triangle")
    print("4) Trapezoid")
    print("5) Circle")
    print("6) Exit")

    choice = input("Enter your choice (1-6) or write name of the figure: ")
    
    if choice == "6" or choice.lower() == "exit":
        print("Exiting the program.")
        break

    elif choice == "1" or choice.lower() == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"The area of the rectangle is: {area_of_rectangle(length, width)}")

    elif choice == "2" or choice.lower() == "square":
        side = float(input("Enter the side of the square: "))
        print(f"The area of the square is: {area_of_square(side)}")

    elif choice == "3" or choice.lower() == "triangle":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"The area of the triangle is: {area_of_triangle(base, height)}")

    elif choice == "4" or choice.lower() == "trapezoid":
        base1 = float(input("Enter the first base of the trapezoid: "))
        base2 = float(input("Enter the second base of the trapezoid: "))
        height = float(input("Enter the height of the trapezoid: "))
        print(f"The area of the trapezoid is: {area_of_trapezoid(base1, base2, height)}")
    
    elif choice == "5" or choice.lower() == "circle":
        radius = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is: {area_of_circle(radius)}")

   
    
    else:
        print("Invalid choice. Please select a valid option.")
        continue
    
    cont = input("Do you want to continue? (yes/no): ").lower()
    if cont != 'yes':
        print("Exiting the program.")
        break