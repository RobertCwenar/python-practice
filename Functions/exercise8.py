'''
def messege(name):
    print (f"Hello, {name}! Welcome to the my programming world!")


list = ["Arkadiuszu", "Jadziu", "Aleksandrze"]

for name in list:
    messege(name)


#example definition:

def area_of_square(side):
    return side * side

print(area_of_square(7))

#return - zwraca wartość z funkcji do miejsca, gdzie funkcja została wywołana
def area_of_rectangle(length, width):
    return length * width

print(area_of_rectangle(7, 10))


def area_of_rectangle(length, width):
    print(length * width)

area_of_rectangle(7, 10)


area_of_rectangle = area_of_rectangle(2,8)
area_of_rectangle2 = area_of_rectangle(24,8)
#print(f"The area of first rectangle is: {area_of_rectangle}")
#print(f"The area of second rectangle is: {area_of_rectangle2}")
'''

def divide(a, b):
    if b == 0:
        return "You can't divide by zero!"
    return a / b

x = (divide(10, 2))
if (x):
    print("Division successful", x)
else:
    print("Error: Division by zero")