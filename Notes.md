
## Python

### Print
```python
print("Hello There")
```

### Input
```python
input("What is your name? ")
```

### Variable
Give a name to a piece of data, like a box with a label. 
Notice a str needs "" and an int doesn't.
```python
my_age = 12
my_name = "NatYolo"
```

### Line Break
To add a paragraph break, a new paragraph put in `\n`
```python
print("Hello World\nHello World")
```
<br>

## Data Types
### Strings
"Abc" or "123" with double or single quotes.
```python
"Hello"
```

### Integer
Whole numbers without decimal places.
```python
int(123)
123 + 456
```

### Float
Floating point number, decimal number.
```python
float(3.14159)
```

### Boolean
Two values, either True or False.
```python
bool(<value>)
True
False
```

### Subscript
Pulling out an element from the string.
```python
print("Hello"[0])
# Output will be: H, "0" is the index in the string.

```

### Checking Data Types
```python
age = 23
type(age)  # This will print out the type of variable: <class 'int'>
```

### Converting Data Types
```python
float(x)
int(y)
str(a)
```
### Length
Returns the length of an object.
```python
len(x)      # Count the number of items in the list, or characters in strings.
print(len("hello"))     # output: 5 characters
print(len(["apple", "grapes", "orange"]))       # output: 3 items
num_char = len(input("What is your name? \n"))
```

### Type
function returns the type of the object.
```python
a = 123
print(type(a))      # Prints and checks data type - which is an int.

a = str(123)        # Prints and converts data type to a str.
print(type(a))

a = float(123)      # Converts to a float.
print(type(a))
```
### F-Strings
can insert different variable into strings.
```python
score = 0           # string
height = 1.8        # float
is_winning = True   # boolean

# Instead of putting + and converting them..
print("Your score is " + str(score) + ", your height is " + str(height) + " and are you winning? " + str(is_winning))

# Just need to add an 'f' and variable inside {}:
print(f"Your score is {score}, your height is {height} and are you winning? {is_winning}")
```
<br>

## Operators
PEMDAS-LR # Remember PEMDASLR (Parentheses, Exponents, Multiply & Divide, Add & Subtract, Left to Right)
```python
3 + 5
7 - 2
3 * 2
6 / 3       # When you divide, you always end up with a float.
2 ** 2      # To the power of 2. Squared.     
()
**
* /
+ -
print(3 * 3 + 3 / 3 - 3)    # This order matters.
```


### Rounding numbers
9 divided by 3, 2 decimals places
```python
(round(9 / 3, 2))
(9 // 2)    # Using // turns this float into an int. no rounding, just remove floats
result = 4 / 2      # 4 / 2 = 2, result is 2.
result /= 2         # getting the result and divide by 2. >> output:1
```
### The `+=` Operator
This is a convenient way of saying: take the previous value and add to it. My age is now 16.
```python
my_age = 12
my_age += 4
```
### Modulo
Modulo operator gives you the remainder result of uneven division
```python
5 % 2  # 2, 2 , 1
# result is 1.

==  # Equal to.
!=  # Not equal to.
>   # Greater than.
<   # Less than.
<=  # Less than or equal to.
>=  # Greater than or equal to.
```

<br>

## Logical Operators
Logical operators are used to combine multiple conditions together and evaluate them as a single boolean expression. There are three types of logical operators in Python: `and`, `or`, and `not`.
<br>

### and
The `and` operator returns `True` if both conditions it is evaluating are true, otherwise it returns `False`.

```python
This expects both conditions either side of the 'and' to be true.
a = 58
if a < 60 and a > 50:
    print("Your grade is C")
```

### or
In Python, the `or` operator is used to combine two or more conditions in a logical expression. The resulting expression evaluates to True if at least one of the conditions is `True`.

```python
x = 5
y = 10

if x < 3 or y > 9:
    print("At least one condition is true")
else:
    print("Both conditions are false")
```

### not
In Python, the keyword `not` is a logical operator that reverses the boolean value of an expression. It can be used with any expression that evaluates to `True` or `False`. <br>
For example, let’s say we have a boolean variable ‘is_raining’ that is True if it’s currently raining and False otherwise. We can use the ‘not’ operator to check if it’s not raining

```python
is_raining = True
if not is_raining:
    print("It's not raining!")
else:
    print("It's raining.")
```
<br>

## If Statements
This is the basic syntax to test if a condition is true. 
If so, the indented code will be executed, if not it will be skipped.
```python
if condition1:
    do x

# In addition to the initial If statement condition, you can add extra conditions to test if the first condition is false. Once an elif condition is true, the rest of the elif conditions are no longer checked and are skipped.

elif condition2:
    do y

# This is a way to specify some code that will be executed if all the above conditions are false:

else:
    do z


condition = True
if condition:
    x = 1
else:
    x = 0
print(x)
```

A shortcut is to put it into one line.
```python
x = 1 if condition is true else 0
```
<br>

### Nested If / Else
```python
if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this
```
<br>

### If / Elif / Else Conditions
you can add extra conditions to test if the initial condition is false.

```python
if condition1:      # condition1 is what we're testing for.
    do A            # < this will be executed if the condition1 is met and skip  all elif and else conditions below.

elif condition2:
    do B
elif condition3:
    do C

else:  # if conditions above aren't met, it will execute this code.
    do this
```
<p>Above are examples of only 1 condition that would be executed.</p>

Below is checking for multiple conditions.
```python
# If none of these conditions is true, then continue without any changes to output.

if condition1:
    print("Do A")
if condition2:
    print("Do B")
if condition3:
    print("Do C")
if condition = false
```
<br>

## Modules
```python
import Day2         # This will import the module, folder, or file.
print(Day2.age)     # This will print out that variable from the file.
```

### Random Numbers
```python
import random
numbers = random.randint(0, 100)
random_float = random.random
```

### Lists

```python
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Kentucky", "California"]
states = states_of_america  # Can create a variable from a list(variable).

(states[0])         # Specifies the item from the list, 0 is Delaware.
(states[-2])        # Index will also go backward.
print(states[0])    # Prints Delaware - Needs brackets inside the list or square brackets.
print(states[0][0]) # Prints D (First letter of the item from that list.)
```

Specifies the indexed item listed, then changes its name.

```python
(states[0]) = "New York"
states.append("New state")  # add an item to the end of the list
states.extend(["New Landtown", "Bobtown", "State1"])  # adds this list to the current list.

# list.index() >> the output will be the index number of the item in the list
states.index("Delaware")  # output for this function will be 0

# List data type and dictionary data type, notice the {} brackets
student_grades_list = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
student_grades_dict = {"Marry": 8.2, "John": 4.2, "Stacey": 5.9}

```
### Dictionaries
Dictionaries are used to store data values in "key:value" pairs.
A dictionary is a collection which is ordered, changeable and do not allow duplicates.

```python
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}  # "brand", "model, "year" are key paired with values
print(thisdict["brand"])  # output: "Ford"

# do not allow duplicate in dictionary data:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}

print(thisdict)         # output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
# there is no year 1964

print(len(thisdict))    # this counts how many keys in the dictionary, which is 3, consisting of "brand", "model, "year" .

# Will add the list together.
mysum = sum(student_grades_list)

length = len(student_grades_dict)
mean = mysum / length
print(mean)

max_grades = max(student_grades_list)
print(max_grades)

print(student_grades_list.count(10.0))  # Counts the amount of times 10 was in the list.

print(random.choice(Name_of_List))  # Can also directly randomly pick from the list.
```


### Loop Function
