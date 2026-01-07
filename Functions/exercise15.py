import copy 

# copy - płytka 
# deepcopy - głęboka kopia
'''
def evil_function(toBeDestroyedList):
    print(id(toBeDestroyedList))

    print(toBeDestroyedList)

myList = [1,4, 2,1, 52,3]

print(id(myList))
evil_function((myList[0:5]))

a = 4 
b = 4

# exercise 15.1
a = [1, 2, 3]

b = a 
b.append(4)

print(a)
print(b)    

# exercise 15.2

a = [1, 2, 3]
b = a.copy()
b.append(4)

print(a)
print(b)

# exercise 15.3

a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(100)
print(a)
'''

# exercise 15.4
# Użj funkcji any() aby określicz czy lista ma liczby parzyste

numbers1 = [1, 3, 5, 7, 9]
numbers2 = [1, 2, 3, 4, 5]
numbers3 = [2, 3, 6, 9]

def any_even(lista):
   return any ([nr % 2 == 0 for nr in lista])

def all_even(lista):
   return all ([nr % 2 == 0 for nr in lista])

print(any_even(numbers1))
print(any_even(numbers2))
print(any_even(numbers3))

if (any_even(numbers1)):
    print("Lista numbers1 ma liczby parzyste")
else:
    print("Lista numbers1 nie ma liczb parzystych")

if (any_even(numbers2)):
    print("Lista numbers2 ma liczby parzyste")
else:
    print("Lista numbers2 nie ma liczb parzystych")

if (any_even(numbers3)):
    print("Lista numbers3 ma liczby parzyste")
else:
    print("Lista numbers3 nie ma liczb parzystych")

# any - jakikolwiek e- funkcja any Sprawdza czy jakikolwiek element w iterowalnym jest prawdziwy

