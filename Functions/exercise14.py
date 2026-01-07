'''
def add(c, amount=1):
    c = c + amount # local variable is in function scope
    print(c)

# global variable are outside functions
c = 2 
add(c)  
print(c) 

listSample = [1, 4, 512, 24]

listSample2 = listSample

listSample2.append(465)

listSample[0] = 99

k = 4
h = 4

c=5
#print(id(c))

def add(c, amount=1):
    print(id(c))
    c = c + amount # local variable is in function scope
    print(id(c))

#add(c)

def append_to_list(some_list, value):
    some_list.append(value)
    print(id(some_list))

print(id(listSample))
append_to_list(listSample, 5)
print(listSample)
'''

# lambda functions

def double(x):
    return x * 2

print(double(5))

my_list = [2, 5, 13, 17, 8, 10, 100, 34, 23, 44]

def even_number(x):
   if x % 2 == 0:
        return x

my_new_list_filtered = list(filter(lambda x: x % 2 ==0 , my_list))
my_new_list_filtered2 = [x for x in my_list if x % 2 == 0]
print(my_new_list_filtered)

print(my_new_list_filtered2)


'''
# exercise 14.1 
data = [[1, 2], [3, 4], [5, 6]]

# Create a generator that returns each sublist increased by 1 for each element.
# Make sure the original data doesn't change.
# Display the result as a list (but the generator should work "lazily")

new_generator = ( [x + 1 for x in sublist] for sublist in data )

print(list(new_generator))
print(data)

# exercise 14.2



#Zrób shallow copy listy b.

#W b zmodyfikuj pierwszy element pierwszej podlisty (b[0][0] = 999).

#Pokaż, co stało się z a.

import copy 
a = [[10, 20], [30, 40]]
b = copy.copy(a)

b[0][0] = 999
print(b)
print(a)

import copy
# exercise 14.3

a = [[1, 2], [3, 4]]

b = copy.deepcopy(a)
b[0][0] = 100

b[1][1] = 200

print(a)
print(b)

# exercise 14.4

#Stwórz generator gen_even zwracający tylko liczby parzyste (użyj generator expression).

#Stwórz listę list_even zwracającą tylko liczby parzyste (użyj list comprehension).

#Pokaż typ obu zmiennych i wypisz ich zawartość.


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

gen_even = (x for x in numbers if x % 2 == 0)

list_even = [x for x in numbers if x % 2 == 0]

print(type(gen_even))
print(list(gen_even))

print(type(list_even))
print(list_even)

# exercise 14.5

numbers = [3, 6, 9, 12, 15, 20, 25]

# Użyj filter + lambda, żeby wybrać tylko liczby podzielne przez 3.
# Następnie użyj map + lambda, żeby każdą wybraną liczbę pomnożyć przez 2.
# W końcu zrób generator expression, który zwraca te wartości leniwie.
# Wyświetl wynik jako listę.

filter1 = filter(lambda x: x% 3 ==0, numbers)

map1 = map(lambda x: x*2, filter1)

gen_even = (x for x in map1)

print(list(gen_even))'''