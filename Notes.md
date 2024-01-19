
# Day 1

## Hello There
```pythonprint("Hello There")```

## Input prompt for the user
```input("What is your name? ")```

## Variables give a name to a piece of data, like a box with a label. Notice a str needs "" and an int doesn't.
```my_age = 12
    my_name = "NatYolo"
```

## The += Operator - This is a convenient way of saying: take the previous value and add to it - my age is now 16.
```my_age = 12
my_age += 4
```

## To add a paragraph break, a new paragraph put in \n
```print("Hello World\nHello World")```

# Data Types
## Strings - "Hey" or "123" with double quotes.
print("Hello")

## Integer - Whole numbers without decimal places.
print(123)
print(123 + 456)

## Float - Floating point number, decimal number.
print(3.14159)

## Boolean - Two values, either True or False.
True
False

## Subscript - pulling out a number from a string.
print("Hello"[0])
# output: H, "0" is the index in the string

# Checking Data Types
age = 23
type(age)  # This will print out the type of variable: <class 'int'>

# Converting Data Types
float()
int()
str()

# len() >> count the number of items in the list, or characters in strings.
print(len("hello"))  # output: 5 characters
print(len(["apple", "grapes", "orange"]))  # output: 3 items

num_char = len(input("What is your name? \n"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = 123
print(type(a))  # Prints and checks data type - which is an int.

a = str(123)  # Prints and converts data type to a str.
print(type(a))

a = float(123)  # Converts to a float.
print(type(a))

print(70 + float("100.5"))  # This will print int AND float.
print(str(70) + str(100))  # This will print the two strings together.

# Day 2, Exercise 1
## Cannot change the code below.
two_digit_number = input("Type a two-digit number: ")
## Cannot change the code above.

# So find the data type, e.g., string, interval, float.
print(type(two_digit_number))

# Pull out the numbers with subscripting.
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

# Turn variables into int and + them together.
result = int(first_digit) + int(second_digit)

# Print the result.
print(result)

3 + 5
7 - 2
3 * 2
6 / 3  # When you divide, you always end up with a float.
2 ** 2  # To the power of 2. Squared.
# PEMDAS-LR # Remember PEMDASLR (Parentheses, Exponents, Multiply & Divide, Add & Subtract, Left to Right)
# ()
# **
# * /
# + -
print(3 * 3 + 3 / 3 - 3)  # This order matters. Use Thonny to see the order.

# Day 2, Exercise 2 (BMI Calculator)
## Cannot change the code below
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
## Cannot change the code above
# print(type(height))
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)

# Rounding numbers - 9 divided by 3, 2 decimals places
print(round(9 / 3, 2))
print(9 // 2)  # Using // turns this float into an int. no rounding, just remove floats

result = 4 / 2  # 4 / 2 = 2, result is 2.
result /= 2  # getting the result and divide by 2. >> output:1

# f-Strings, can insert different variable into strings.
score = 0  # string
height = 1.8  # float
is_winning = True  # boolean
# Instead of putting + and converting them, just add and f-string.
print("Your score is " + str(score) + ", your height is " + str(height) + " and are you winning? " + str(is_winning))

# Just need to add an 'f' and variable inside {}
print(f"Your score is {score}, your height is {height} and are you winning? {is_winning}")

# Day 2, Exercise 3 (Your life in weeks)
age = int(input("What is your current age? "))

years_remaining = 90 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left until you are 90 years old."

print(message)

# DAY 3
# This is the basic syntax to test if a condition is true. If so, the indented code will be
# executed, if not it will be skipped.
if condition1:
    do A

# In addition to the initial If statement condition, you can add extra conditions to
# test if the first condition is false. Once an elif condition is true, the rest of
# the elif conditions are no longer checked and are skipped.
elif condition2:
    do B

# This is a way to specify some code that will be executed if all the above conditions are false.
else:
    do C

# Example below
condition = True
if condition:
    x = 1
else:
    x = 0
print(x)

# A shortcut is to put it into one line. Shown below.
x = 1 if condition is true else 0

# Nested if / else
if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this

# if / elif / else condition - you can add extra conditions to test if the initial condition is false.
if condition1:  # condition1 is what we're testing for.
    do A  # < this will be executed if the condition1 is met and skip all elif and else conditions below.
elif condition2:
    do B
elif condition3:
    do C
else:  # if conditions above aren't met, it will execute this code.
    do this

# Above are examples of only 1 condition that would be executed.
# Below is checking for multiple conditions (if none of these conditions is true, then continue without any changes to output):

if condition1:
    print("Do A")
if condition2:
    print("Do B")
if condition3:
    print("Do C")

OR
if condition = false

# Also use this += operator. Adds the value back onto the variable.
bill += 3
# Same as..
bill = bill + 3

# Greater

 than, Lesser than, Greater than or equal to, Lesser than or equal to, Is equal to, Is not equal to (!=)
# Modulo operator gives you the remainder result of uneven division
5 % 2  # 2, 2 , 1
# result is 1.

# Logical operators: AND, OR and NOT
# AND
# This expects both conditions either side of the 'and' to be true.
a = 58
if a < 60 and a > 50:
    print("Your grade is C")

# OR
# If you only needed one of the conditions to be true.
# This expects either of the conditions either side of the or to be true.
age = 12
if age < 16 or age > 200:
    print("Can't drive")

# NOT
# This will flip the original result of the condition, e.g., if it was true then, now it's false.
if not 3 > 1:
    print("something")  # Will not be printed.

# MODULES
import Day2  # This will import the module, folder, or file.
print(Day2.age)  # This will print out that variable from the file. syntax == file.variable

# Random Numbers
import random
numbers = random.randint(0, 100)
random_float = random.random

# Lists
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Kentucky", "California"]
states = states_of_america  # Can create a variable from a list(variable).

(states[0])  # Specifies the item from the list, 0 is Delaware.
(states[-2])  # Index will also go backward.
print(states[0])  # Prints Delaware - Needs brackets inside the list or square brackets.
print(states[0][0])  # Prints D (First letter of the item from that list.)

# Specifies the indexed item listed, then changes its name.
(states[0]) = "New York"

states.append("New state")  # add an item to the end of the list
states.extend(["New Landtown", "Bobtown", "State1"])  # adds this list to the current list.

# list.index() >> the output will be the index number of the item in the list
states.index("Delaware")  # output for this function will be 0

# List data type and dictionary data type, notice the {} brackets
student_grades_list = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
student_grades_dict = {"Marry": 8.2, "John": 4.2, "Stacey": 5.9}

# Dictionaries are used to store data values in "key:value" pairs.
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}  # "brand", "model, "year" are key paired with values
print(thisdict["brand"])  # output: "Ford"

# do not allow duplicate in dictionary data:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)  # output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
# there is no year 1964

print(len(thisdict))  # this counts how many keys in the dictionary, which is 3, consisting of "brand", "model, "year" .

# Will add the list together.
mysum = sum(student_grades_list)

length = len(student_grades_dict)
mean = mysum / length
print(mean)

max_grades = max(student_grades_list)
print(max_grades)

print(student_grades_list.count(10.0))  # Counts the amount of times 10 was in the list.

print(random.choice(Name_of_List))  # Can also directly randomly pick from the list.

# DAY 5

# For Loop Function
# For item in the list of items
# repeat the same task for all items in the list
# item in the function could be any name that we use to refer to an item in the list.

fruits = ["apple", "grapes", "rambutan"]
for fruit in fruits:
    print(fruit)
# output from the example will be:
# apple
# grapes
# rambutan

# what the code does basically assign the "fruit" as variable to each item and order it to print each one. >> check Thonny

# *** Be careful with the indentation. Check your task whether it is inside/outside For loop

fruits = ['apple', 'grapes', 'guava']
for fruit in fruits:
    print(fruit)  # 2 tasks print fruit and fruits >> look at the indentation >> this is inside the for loop
    print(fruits)

# the list there are 3 items, this set will be repeated 3 times for each item in the list
# output:
# apple
# ['apple', 'grapes', 'guava']
# grapes
# ['apple', 'grapes', 'guava']
# guava
# ['apple', 'grapes', 'guava']

# the task is outside the For loop

fruits = ['apple', 'grapes', 'guava']
for fruit in fruits:
    print(fruit)  # inside the for loop
print(fruits)  # outside the for loop

# each item in the list will be printed. Once it prints all 3 items in the list >> the for loop function is completed
# then the next line of code will be executed.

# output:
# apple
# grapes
# guava
# ['apple', 'grapes', 'guava']

# Remember?
# split() function >> "string".split()
# it returns a list of all the words in the string, using str as the separator
# (splits on all whitespace if left unspecified), optionally limiting the number of splits to num.
