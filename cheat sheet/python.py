# ----------------------Variables-----------------------
a = 10
b = "hello"
c = True

# ----------------------Data types----------------------
integer_num = 10
float_num = 3.14
string = "hello world"
boolean = True
list_of_numbers = [1, 2, 3, 4, 5]
tuple_of_numbers = (1, 2, 3, 4, 5)
dictionary = {'a': 1, 'b': 2, 'c': 3}


# In Python, if you want to print two different elements in the same line we have to use a " , " between them.
# This acts as a separator and helps the code to run without errors.


# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

# 5 is an integer, but "5" is a string containing the character '5'. They are different entities.

# ----------------------Arithmetic Operators----------------------
x = 10 + 5 # 15
y = 10 - 5 # 5
z = 10 * 5 # 50
q = 10 / 5 # 2.0
r = 10 % 3 # 1
s = 10 ** 2 # 100


# ----------------------Comparison Operators----------------------
a == b # True if a is equal to b
a != b # True if a is not equal to b
a < b  # True if a is less than b
a > b  # True if a is greater than b
a <= b # True if a is less than or equal to b
a >= b # True if a is greater than or equal to b


# ----------------------Logical Operators----------------------
a and b # True if both a and b are True
a or b  # True if either a or b is True
not a   # True if a is False


# The command used to take input from the user in python is called input().
# This will typically be stored in a variable.


# All inputs in Python are by default assumed to be strings.
# But if we want to input an integer from the user, we will have to explicitly tell Python to convert the input string to an int.
# So we write "int(input())" instead of just "input()".


# ----------------------If statement----------------------
if condition:
    # code block to execute if condition is True

# If-else statement
if condition:
    # code block to execute if condition is True
else:
    # code block to execute if condition is False

# If-elif-else statement
if condition1:
    # code block to execute if condition1 is True
elif condition2:
    # code block to execute if condition2 is True
else:
    # code block to execute if both condition1 and condition2 are False

# For loop
for variable in sequence:
    # code block to execute for each value of variable in sequence

# While loop
while condition:
    # code block to execute while condition is True

# Break and continue statements
for variable in sequence:
    if condition:
        break  # exit loop
    if condition:
        continue  # skip current iteration



# ----------------------Defining a function----------------------
def function_name(arguments):
    # code block to execute when function is called

# Calling a function
function_name(arguments)

# Returning a value from a function
def function_name(arguments):
    # code block to execute when function is called
    return value

# --------------------------------Passing a function as an argument---------------------------------
def function_one():
    return "Hello, "

def function_two():
    return "World!"

def function_three(func):
    return func()

result = function_three(function_one) + function_three(function_two)
print(result) # "Hello, World!"



#---------------------- Reading from a file----------------------
with open('file.txt', 'r') as f:
    contents = f.read()

# Writing to a file
with open('file.txt', 'w') as f:
    f.write('Hello, World!')

# Appending to a file
with open('file.txt', 'a') as f:
    f.write('Hello, again!')



# -------------------------------------------------------------------------
# The process of joining two strings is called concatenation.
# We can join the strings very easily by using the '+' operator.

# Concatenating strings
a = "hello"
b = "world"
c = a + " " + b # "hello world"

# String formatting
name = "Alice"
age = 25
greeting = "My name is {} and I'm {} years old".format(name, age) # "My name is Alice and I'm 25 years old"

# String methods
# The upper() command returns the string in upper case
# The lower() command returns the string in lower case
# The replace(string1, string2) command replaces all occurrences of string1 with string2.
    # So, for example, if s = "abcd", then s.replace("bc", "xy") would be "axyd".
    # Similarly, if s = "abcdbc", then s.replace("bc", "z") would be "azdz".

message = "hello world"
message_upper = message.upper() # "HELLO WORLD"
message_lower = message.lower() # "hello world"
message_length = len(message) # 11


# You can get some consecutive characters of a string by using the 'slice' syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# The first character has an index 0.
# If you don't specify the starting index, it takes it from the beginning of the string.
# Similarly, if you don't specify the ending index, it considers till the end of the string.
# Remember that blank space in a string is also a character!!!


# Indexing and slicing lists

    # Indexing always start from 0 when going left to right.
    # Indexing always starts from −1 when going right to left.
numbers = [1, 2, 3, 4, 5]
first_number = numbers[0] # 1
last_number = numbers[-1] # 5
middle_numbers = numbers[1:4] # [2, 3, 4]

# Modifying lists
numbers.append(6) # [1, 2, 3, 4, 5, 6]
numbers.insert(2, 7) # [1, 2, 7, 3, 4, 5, 6]
# To insert a list item at a specified index, we can use the insert() method which does the following
    # Inserts an item at the specified index
    # All the elements after this item are shifted to the right
numbers.remove(3) # [1, 2, 7, 4, 5, 6]

# List objects have a sort() method that will sort the list alphanumerically, and in ascending order by default.

# A list containing only strings -
    # for example ["b", "d", "c", "a"] when sorted will return the list ["a", "b", "c", "d"]
# A list containing only numbers - 
    # for example [5, 4, 3, 2, 1] when sorted will return the list [1, 2, 3, 4, 5]
# A list containing both strings and numbers - 
    # for example ["b", "d", "c", 1] will return a runtime error if we try and run the sort() operation on it

# If you want to sort the list in a descending order, you have to use the syntax list_name.sort(reverse=True).


# There are multiple ways of deleting elements from a List.

# The pop() method removes the item with the specified index number.
# The remove() keyword removes the item with the specified name.
# The clear() method empties the List.




# We can use the append() method to add an element at the end of a list.

# On the flip side if we want to remove the last element of a list 
# we use the pop() method without providing any index.


# List comprehensions
squares = [x**2 for x in numbers if x % 2 == 0] # [4, 49, 16, 36]


# Accessing dictionary values
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
name = person['name'] # 'Alice'
age = person.get('age') # 25

# Adding and modifying dictionary values
person['city'] = 'Los Angeles'
person['occupation'] = 'engineer'

# Looping over dictionaries
for key, value in person.items():
    print(key, value)

# Dictionary comprehensions
squares = {x: x**2 for x in numbers if x % 2 == 0} # {2: 4, 4: 16, 6: 36}


#  ------------------------------------Defining a class ------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print("Hello, my name is {} and I'm {} years old".format(self.name, self.age))

#  ------------------------------------Creating an object ------------------------------------
person = Person('Alice', 25)
person.say_hello() # "Hello, my name is Alice and I'm 25 years old"


#  ------------------------------------Importing a module ------------------------------------
import math
pi = math.pi # 3.141592653589793
sqrt = math.sqrt(4) # 2.0

#  ------------------------------------Importing from a module ------------------------------------
from math import pi, sqrt
pi = pi # 3.141592653589793
sqrt = sqrt(4) # 2.0

#  ------------------------------------Creating a package ------------------------------------
my_package/
    __init__.py
    module_one.py
    module_two.py

#  ------------------------------------Importing from a package ------------------------------------
from my_package.module_one import my_function
result = my_function()


# Dictionaries are used to store data values in key:value pairs. 
# A dictionary is a collection that is ordered, changeable and does not allow duplicates.


# You can think of this as a generalisation of lists.


# In lists, the index numbers point to the values. But there the index numbers were restricted to be 0, 1, 2, ...
# In dictionaries, your keys can be anything you want. Keys are a generalisation of index numbers.
# You can access the items of a dictionary by using the get() keyword.


# There are multiple ways of printing different elements of a dictionary


# The values() method will return a list of all the values in the dictionary.
# The items() method will return each item in a dictionary, as (key, value) tuples in a list.
# You can also change the value of a specific item by referring to its key name.


# Adding an item to the dictionary can be done by using a new index key and assigning a value to it. 


# The pop() method removes the item with the specified key name:
# The del keyword removes the item with the specified key name and can also delete the whole dictionary
# The clear() method empties the dictionary


# With the "continue" statement we achieve the following:
    # We can stop the current iteration of the loop
    # We continue with the next element. That is, we will not go any further in this particular iteration, and instead skip to the next iteration.


# We can use the "break" statement to stop the loop before it has looped through all the items.


# break" functions differently from "continue" that we learnt earlier
# "break" exits the loop completely and goes to the next section of the program
# "continue" exits the current iteration and skips the code remaining in the current loop iteration.
# However, the "for" or "while" loop continues with the next iteration.


# A nested loop is a loop inside a loop.
# The "inner loop" will be executed completely for each single iteration of the "outer loop":


# The way to accept multiple integers in a single line is to use the split and map function.
    # split function breaks the input based on the separator - by default, it splits inputs separated by spaces in a single line into different inputs which you can assign to different variables
    # map function converts each input into the defined datatype






