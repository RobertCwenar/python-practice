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
'''
# exercise 15.3

a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(100)
print(a)