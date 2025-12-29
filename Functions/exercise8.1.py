import enum
import figures as fi
#enumeration - spis - wyliczenie
#IntEnum - integer enumeration - wyliczenie liczbowe

#Enum: zwiększa czytelność kodu; nie popełniamy błędów literówek; podpowiedz z edytora
from enum import IntEnum
'''
Menu_Figures = IntEnum('Menu_Figures', ['Square', 'Rectangle', 'Circle', 'Triangle', 'Trapezoid'])

choose = int(input(""" Choose the figure to calculate area: 
1. Square
2. Rectangle
3. Circle
4. Triangle
5. Trapezoid
Enter the number corresponding to your choice: """))

if choose == Menu_Figures.Square:
    side = float(input("Enter the side length of the square: "))
    print(f"Area of the square is: {fi.area_of_square(side)}")

elif choose == Menu_Figures.Rectangle:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print(f"Area of the rectangle is: {fi.area_of_rectangle(length, width)}")

elif choose == Menu_Figures.Circle:
    radius = float(input("Enter the radius of the circle: "))
    print(f"Area of the circle is: {fi.area_of_circle(radius)}")

elif choose == Menu_Figures.Triangle:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print(f"Area of the triangle is: {fi.area_of_triangle(base, height)}")

elif choose == Menu_Figures.Trapezoid:
    base1 = float(input("Enter the first base of the trapezoid: "))
    base2 = float(input("Enter the second base of the trapezoid: "))
    height = float(input("Enter the height of the trapezoid: "))
    print(f"Area of the trapezoid is: {fi.area_of_trapezoid(base1, base2, height)}")
'''
from enum import Enum

class Menu_Weeks(Enum):
    Monday = (1, 'yellow')
    Tuesday = (2, 'green')
    Wednesday = (3, 'blue')
    Thursday = (4, 'purple')
    Friday = (5, 'orange')
    Saturday = (6, 'pink')
    Sunday = (7, 'red')

while True:
    day = int(input("""Choose the day of the week:
    1. Monday
    2. Tuesday  
    3. Wednesday
    4. Thursday
    5. Friday
    6. Saturday
    7. Sunday  
    Enter the number corresponding to your choice: """))

    if day == Menu_Weeks.Monday.value[0]:
        print(f"You chose Monday and the color for that day is {Menu_Weeks.Monday.value[1]}.")
    elif day == Menu_Weeks.Tuesday.value[0]:
        print(f"You chose Tuesday and the color for that day is {Menu_Weeks.Tuesday.value[1]}.") 
    elif day == Menu_Weeks.Wednesday.value[0]:
        print(f"You chose Wednesday and the color for that day is {Menu_Weeks.Wednesday.value[1]}.")
    elif day == Menu_Weeks.Thursday.value[0]:
        print(f"You chose Thursday and the color for that day is {Menu_Weeks.Thursday.value[1]}.")    
    elif day == Menu_Weeks.Friday.value[0]:
        print(f"You chose Friday and the color for that day is {Menu_Weeks.Friday.value[1]}.")
    elif day == Menu_Weeks.Saturday.value[0]:
        print(f"You chose Saturday and the color for that day is {Menu_Weeks.Saturday.value[1]}.")
    elif day == Menu_Weeks.Sunday.value[0]:
        print(f"You chose Sunday and the color for that day is {Menu_Weeks.Sunday.value[1]}.")  