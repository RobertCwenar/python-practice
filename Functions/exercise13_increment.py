'''def increment(x, amount=1):
    return x + amount

print(increment(5))        # Should print 6
'''
# Key arguments and positional arguments
# key - are names of the arguments used in the function definition
# Positional arguments - are arguments passed to the function based on their position
'''
def great(name, message, separator=" "):
    print(message, name, sep=separator)

great(message="Hello in Python", name="Krzysztof")  # Should print: Hello Krzysztof, Hello in Python

# library time
import time 

# Function to measure time taken by each function
def function_performance(func, how_many_times=1, *args, **kwargs):
    total_time =0 

    for i in range(how_many_times):
        start= time.perf_counter()
        func(*args, **kwargs) # if you want to create a function you use () after the function name
        end =time.perf_counter()
        total_time = total_time + (end - start)
    return total_time 

# Two containers: set and list
setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]

# funkcja, która sprawdza czy dana wartość np 30 znajduje sie w liście lub kontenerze set
# Jezeli znajduje się to ma zwrócić Tak jeżeli nie to Nie 
# Tez sprawdzić co jest szybsze w działaniu

# Check the element in the container
def check_element(element, container):
    return "It is in the Container" if element in container else "It isn't in the Container"



# Number to check 
element_in_set = 30
element_in_list = 30


# Test the function
set_result = check_element(element_in_set, setContainer)
set_time = function_performance(check_element, 1, element_in_set, setContainer)
print(f"Number {element_in_set}:", set_result, "\nand the Time taken is:", set_time)

list_result = check_element(element_in_list, listContainer)
list_time = function_performance(check_element, 1, element_in_list, listContainer)
print(f"Number {element_in_list}:", list_result, "\nand the Time taken is:", list_time)
'''


# Write a function that, for example, when called:
# print(count(2,4,1,2,4,5, 10))
# shows as result: 28 for sum of all arguments

def count(*args):
    total =0
    for num in args:
        total += num 
    return total 

print(count(2,4,1,2,4,5, 11))  # Should print 28