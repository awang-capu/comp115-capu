"""
Lab 7 - Strings and Tuples 
(100 marks in total)

Author:  <your name>
Due Date: This Friday (Mar. 6) 5 pm.
Submission: Upload your lab python file to your GitHub repository.

Objective:
1. Learn how to write a good python docstring for documenting functions'
purpose, parameters, return values. A good docstring helps other developers 
understand how to use the function and serves as documentation that can be 
displayed in tools like IDEs. A sample docstring has been written for exercise 1 and 2,
students need to write good docstrings for all the other exercises.
2. Review how to code simple Python functions and write unit tests using assert
3. Practice how to operate on strings and tuples (similar to lists, but strings and tuples are immutable)
4. Review iterations using loop
5. Review the boolean expression and conditionals
6. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, a string, etc.; 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Exercise 1 (10 marks: function implementation: 5 marks, unit tests: 5 marks)

Complete the function below to reverse a string.

For example, 
reverse_str("Abd") should return "dbA".
reverse_str("COMP115") should return "511PMOC".

Hint: the accumulator algorithm and the string concatenation using the operator '+'
"""
def reverse_str(s):
    """
    This function reverses string s.

    E.g., 
    >>> reverse_str('app')
    'ppa'
    """
    result = ''
    for c in s:
        result = c + result
    return result
    
    
# Your unit tests

assert reverse_str("Abd") == "dbA"
assert reverse_str("COMP115") == "511PMOC"


"""
Exercise 2 (10 marks: function implementation: 5 marks, unit tests: 5 marks)

Complete the function below to count how many vowels ('a', 'e', 'i', 'o', 'u') in a string.

For example, 
count_vowels("Apple") should return 2, since 'A' and 'e' are vowels.
count_vowels("Hmmm") should return 0, since there are no vowels.

Hint: you may want to convert the input string to its lowercase version using s.lower() first.
"""
vowels = "aeiou" # "aeiouAEIOU" # ('a', 'e', 'i', 'o', '')

def count_vowels(s):
    """
    This function counts the number of vowels in the string s.

    E.g., 
    >>> count_vowels("Apple")
    2
    """
    count = 0
    for c in s:
        if c.lower() in vowels:
            count += 1
    return count
    

# Your unit tests
assert count_vowels("Apple") == 2
assert count_vowels("Hmmm") == 0


"""
Exercise 3 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to remove the duplicate characters in a string.

E.g.,
remove_duplicates("apple") == "aple"
remove_duplicates("Popsipple") == "Popsile" (Notice: 'P' and 'p' are different chars)
remove_duplicates("pear") == "pear"

"""
def remove_duplicates(s):
    """
    Return a string with duplicate characters removed, keeping the first occurrence.

    E.g.,
    >>> remove_duplicates("apple")
    'aple'
    >>> remove_duplicates("pear")
    'pear'
    """
    result = ''
    for c in s:
        if c not in result: 
            result += c # result = result + c
    return result


# Your unit tests
assert remove_duplicates("apple") == "aple"
assert remove_duplicates("pear") == "pear"



"""
Exercise 4 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the lowest index of a charactor t found in a string s, 
to return -1 if the character is not in the string.

E.g.,
find_index("Abd", 'b') == 1
find_index("Abdccc", 'c') == 3
find_index("Abd", 'w') == -1

Note: we should implement our own algorithm, not using the built-in function s.find(t).
"""
def find_index(s, t):
    """
    Return the index of the first occurrence of t in s, or -1 if not found.

    E.g.,
    -------
    >>> find_index("hello", "l")
    2
    >>> find_index("Abdccc", 'c')
    3

    """
    # for i in range(len(s)):
    #     if s[i] == t:
    #         return i
        
    # return -1

    i = -1
    for c in s:
        i += 1 
        if c == t:
            return i
    return -1




# def find_index(s, t):
#     found = -1
#     for i in range(len(s)):
#         if s[i] == t:
#             found = i
#             break
#     return found

# Your unit tests
assert find_index("Abd", 'b') == 1
assert find_index("Abdccc", 'c') == 3
assert find_index("Abd", 'w') == -1

"""
Exercise 5 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the project completion day, 
given the current day in a week and estimated time of days to completion.

E.g.,
project_completion_day('Monday', 4) returns 'Friday'.
project_completion_day('Monday', 7) returns 'Monday'.
project_completion_day('Saturday', 2) returns 'Monday'.
project_completion_day('Saturday', 1) returns 'Sunday'.

Hint:
days_week.index(day) will return the index of the day in the tuple days_week.

"""

days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday', 'Sunday')
# Notice that days_week is a tuple, and it works the same if it's a list,
# since the index operation is the same for tuple and list.


def project_completion_day(day, days_to_completion):
    """
    Calculate and return the day of the week when a project will be completed.

    E.g., 
    >>> project_completion_day("Monday", 3)
    'Thursday'
    >>> project_completion_day("Friday", 10)
    'Monday'
    """
    today = find_index(days_week, day) #today = days_week.index(day)
    return days_week[(today + days_to_completion) % 7]

# Your unit tests
assert project_completion_day('Monday', 4) == 'Friday'
assert project_completion_day('Monday', 7) == 'Monday'
assert project_completion_day('Saturday', 2) == 'Monday'
assert project_completion_day('Saturday', 1) == 'Sunday'


"""Log Parsing Exercise (20 marks - function implementation 10, unit test 5, function usage 5)

You are given a log string containing application logs 
in a standardized format. Each log entry contains 
a timestamp, severity level, module name, and message.
Your task is to implement two functions to parse and filter
these logs.

Log format - Each log line follows this pattern:
YYYY-MM-DD HH:MM:SS [LEVEL] module.py Message

Sample log data:
log_string = "2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s
2024-03-05 14:32:18 [WARNING] api.py Slow query detected (2.3s)
2024-03-05 14:32:22 [INFO] server.py Server started on port 8000
2024-03-05 14:32:45 [ERROR] database.py Connection lost to primary
2024-03-05 14:33:02 [WARNING] cache.py Redis connection unstable
2024-03-05 14:33:15 [ERROR] api.py Request handler crashed
2024-03-05 14:33:22 [INFO] database.py Attempting reconnect"

Implement a function parse_log_line(line) to parse a single log line into its components.

Your function returns:
A tuple of 4 elements: (timestamp, level, module, message)

timestamp (str): Date and time in format "YYYY-MM-DD HH:MM:SS"
level (str): Log severity level ("ERROR", "WARNING", or "INFO")
module (str): The Python module/file name (e.g., "database.py")
message (str): The log message text

E.g.,
line = '2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s'
parse_log_line(line) == ('2024-03-05 14:32:15', 'ERROR', 'database.py', 'Connection timeout after 30s')

Hints: 

1. str.split() returns a list of strings, split by default (whitespace).
"hello world python".split()
# Returns: ['hello', 'world', 'python']

2. string concatenation
'I like ' + 'you'
# Returns 'I like you'

3. str.join()
list = ['Hello, ', 'world!']
' '.join(list)
# Returns 'Hello,  world!'
"""

def parse_log_line(line):
    parts = line.split()
    #print(parts)
    return (parts[0] + ' ' + parts[1], parts[2][1:-1], parts[3], ' '.join(parts[4:]))
    # return (' '.join(parts[:2]), parts[2][1:-1], parts[3], ' '.join(parts[4:]))



# Your unit tests
line1 = '2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s'
assert parse_log_line(line1) == ('2024-03-05 14:32:15', 'ERROR', 'database.py', 'Connection timeout after 30s')

# line2 = '2024-03-05 14:32:18 [WARNING] api.py Slow query detected (2.3s)'
# assert parse_log_line(line2) == ('2024-03-05 14:32:18', 'WARNING', 'api.py', 'Slow query detected (2.3s)')

# line7 = '2024-03-05 14:33:22 [INFO] database.py Attempting reconnect'
# assert parse_log_line(line7) == ('2024-03-05 14:33:22', 'INFO', 'database.py', 'Attempting reconnect')


# Use your parse_log_line() to parse all the lines in the sample data log_string,
# and store each tuple item in a list.
# Hint: log_string.split('\n') will return a list of lines.


log_string = """2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s
2024-03-05 14:32:18 [WARNING] api.py Slow query detected (2.3s)
2024-03-05 14:32:22 [INFO] server.py Server started on port 8000
2024-03-05 14:32:45 [ERROR] database.py Connection lost to primary
2024-03-05 14:33:02 [WARNING] cache.py Redis connection unstable
2024-03-05 14:33:15 [ERROR] api.py Request handler crashed
2024-03-05 14:33:22 [INFO] database.py Attempting reconnect"""
lines = log_string.split('\n')
list_lines = []
for line in lines:
    t = parse_log_line(line)
    list_lines.append(t)
print(list_lines)

count_error = 0
for t in list_lines:
    if t[1] == 'ERROR':
        count_error += 1
print(count_error)


# lines = log_string.split('\n')
# entry_list = []
# for line in lines:
#     entry_list.append(parse_log_line(line))
# print(entry_list)

# Now you can use what you've learnt about accumulator algorithm to do more data analyzing. 
# For example, to count how many ERROR logs there:
# count_error = 0
# for entry in entry_list:
#     if entry[1] == 'ERROR':
#         count_error += 1
# print(count_error)



"""
Congratulations on finishing your lab7. Hope you feel more confident 
on function implementation.

Now you just need to upload it to your GitHub repository. That's all.
"""
