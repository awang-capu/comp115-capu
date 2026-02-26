"""
Lab 6 - Selections and Iterations 
(100 marks in total, including 7 exercises)

Author:  <your name>
Due Date: This Friday (Feb. 13) 5pm.

Objective:
1. Practice coding simple Python functions and writing unit tests testing functions by assert
2. Practice how to operate on lists
3. Practice with iterations using loop
4. Practice using the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, etc. 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
5. Practice with selections, boolean expressions and boolean functions.
"""



"""
Exercise 1 (10 marks)

Implement a function is_in_list(nums, k) that checks 
whether the number k exists in the list nums.
If k is in nums, return True.
Otherwise, return False.
"""
def is_in_list(nums, k):
    for num in nums:
        if num == k:
            return True
    return False

assert is_in_list([4, 5, 6], 5) == True
assert is_in_list([], 3) == False
assert is_in_list([-3, -2, -1, 0], -1) == True



"""
Exercise 2 (10 marks)

Write a function has_negative(nums)
that returns True if the list contains any negative number,
otherwise False.
"""

def has_negative(nums):
    for num in nums:
        if num < 0:
            return True
        
    return False

assert has_negative([1, 2, 3, -4, 5]) == True
assert has_negative([0, 2, 3, 4, 5]) == False


"""
Exercise 3 (10 marks)

Write a function all_even(nums) 
that returns True if all numbers in the list are even,
otherwise False.

"""

def all_even(nums):
    for num in nums:
        if num % 2 == 1:
            return False
    return True


assert all_even([2, 4, 6, 8]) == True
assert all_even([2, 3, 4]) == False


"""
Exercise 4 (10 marks)

Write a function count_even_odd(nums) that counts how many numbers
in a list are even and how many are odd. 

Return a list [even_count, odd_count]
"""
def count_even_odd(nums):
    even_count = 0
    odd_count = 0
    for num in nums:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return [even_count, odd_count]

assert count_even_odd([1, 2, 3, 4, 5, 6]) == [3, 3]
assert count_even_odd([2, 4, 6, 8]) == [4, 0]
assert count_even_odd([1, 3, 5]) == [0, 3]


"""
Exercise 5 (10 marks)

Write a function temp_category(temps) that
categorizes temperatures with an input of list of temperatures:

≥30 → "hot"

15-29 → "mild"

<15 → "cold"

Return a list [hot_count, mild_count, cold_count]

"""

def temp_category(temps):
    hot_count = 0
    mild_count = 0
    cold_count = 0
    for temp in temps:
        if temp >= 30:
            hot_count += 1
        elif temp >=15:
            mild_count += 1
        else:
            cold_count += 1
    return [hot_count, mild_count, cold_count] 

assert temp_category([32, 28, 15, 12, 35]) == [2, 2, 1]
assert temp_category([10, 5, 0]) == [0, 0, 3]
assert temp_category([20, 25, 30]) == [1, 2, 0]




"""
Exercise 6 (10 marks)

Write a function mult_category(nums) that categorizes
each number in the list according to the following rules:

Multiple of 2 → append 2
Multiple of 3 → append 3
Multiple of 5 → append 5
If a number is not a multiple of 2, 3, or 5 → append the letter "O"

Return a list of the categories.
"""

def mult_category(nums):
    res = []
    for num in nums:
        if num % 2 == 0:
            res.append(2)
        elif num % 3 == 0:
            res.append(3)
        elif num % 5 == 0:
            res.append(5)
        else:
            res.append('O')

    return res

assert mult_category([2, 3, 5, 7]) == [2, 3, 5, "O"]
assert mult_category([4, 9, 10, 11]) == [2, 3, 2, "O"]
assert mult_category([15, 7, 30, 11]) == [3, "O", 2, "O"]


"""
Exercise 7 (10 marks)

Implement a function to reverse a list.

"""
def reverse_list(nums):
    res = []
    n = len(nums)
    for i in range(n):
        res.append(nums[n - 1 - i])
    return res

# def reverse_list(nums):
#     res = []
#     n = len(nums)
#     for i in range(n - 1, -1, -1):
#         res.append(nums[i])
#     return res

# def reverse_list(nums):
#     n = len(nums)
#     for i in range(n // 2 + 1):
#         temp = nums[i]
#         nums[i] = nums[n - 1 - i]
#         nums[n - 1 - i] = temp
#     return nums

assert reverse_list([1, 3, 4]) == [4, 3, 1]
assert reverse_list([3, 9, 6]) == [6, 9, 3]


"""
Exercise 8 (10 marks)

Implement a function that returns a new list with
all duplicate values removed from the input list.
The order of the first occurrences should be preserved.

Hint:

The expression 
num in nums
is True if num exists in the list nums.

The expression 
num not in nums
is True if num does not exist in the list nums.
"""
def remove_duplicates(nums):
    res = []
    for num in nums:
        if num not in res:
            res.append(num)
    return res

assert remove_duplicates([1, 3, 3, 4]) == [1, 3, 4]
assert remove_duplicates([1, 1, 3, 4, 3]) == [1, 3, 4]


"""
Exercise 9 (10 marks)

Write a function my_factorial(n) that returns the factorial 
of a non-negative integer n.

Factorial rule:
0! = 1
1! = 1
n! = n * (n-1) * (n-2) * ... * 1

You may assume n >= 0.

"""
def my_factorial(n):
    if n == 0:
        return 1
    res = 1
    for i in range(n, 0, -1): #range(1, n + 1, 1):
        res *= i
    return res

assert my_factorial(0) == 1
assert my_factorial(1) == 1
assert my_factorial(3) == 6
assert my_factorial(5) == 120

"""
Exercise 10 (10 marks)

Write a function my_fib(n) that returns a list containing the first n Fibonacci numbers.

Fibonacci rule:
Start with [0, 1]
Each next number is the sum of the previous two
If n = 1, return [0]
If n = 2, return [0, 1]
If n = 3, return [0, 1, 1]
If n = 4, return [0, 1, 1, 2]
"""
def my_fib(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        res = [0, 1]
        for i in range(2, n):
            res.append(res[-1] + res[-2])
            #res.append(res[i - 1] + res[i - 2])
        return res


assert my_fib(1) == [0]
assert my_fib(2) == [0, 1]
assert my_fib(5) == [0, 1, 1, 2, 3]
assert my_fib(7) == [0, 1, 1, 2, 3, 5, 8]

"""
Congratulations on finishing your lab6!
Now upload to your GitHub repository, and paste your GitHub link on e-learn.

Have a great reading break!
"""