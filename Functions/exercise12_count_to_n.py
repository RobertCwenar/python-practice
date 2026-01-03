# Write a program that calculates the sum of all numbers from 1 to a given number n entered by the user.
# For example, for 5 the program should return 15 (1+2+3+4+5).

# Function to calculate the sum from 1 to n
def sum_to_n(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

# Test 1 function using list comprehension
def test1_sum_to_n(n):
    return sum([n for n in range(1, n + 1)])

# Test 2 function using set comprehension
def test2_sum_to_n(n):
    return sum({n for n in range(1, n + 1)})

# Test 3 function using generator expression
def test3_sum_to_n(n):
    return sum((n for n in range(1, n + 1)))

# Test 4 function using the formula n(n + 1)/2
def test4_sum_to_n(n):
   return (1 + n)/ 2 * n

# Main program
if __name__ == "__main__":
    n = int(input("Enter a number n: "))
    result1 = sum_to_n(n)
    result2 = test1_sum_to_n(n)
    result3 = test2_sum_to_n(n)
    result4 = test3_sum_to_n(n)
    result5 = test4_sum_to_n(n)

    print(f"Sum of consecutive numbers from 1 to {n} is: {result1}")
    print(f"Test 1 result: {result2}")
    print(f"Test 2 result: {result3}")
    print(f"Test 3 result: {result4}")
    print(f"Test 4 result: {result5}")