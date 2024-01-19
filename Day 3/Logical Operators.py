#   Logical operators: AND , OR and NOT

#   AND
#   This expects both conditions either side of the 'and' to be true.
a = 58
if a < 60 and a > 50:
    print("Your grade is C")


#   OR
#   If you only needed one of the conditions to  be true.
#   This expects either of the conditions either side of the or to be true.
age = 12
if age < 16 or age > 90:
    print("Can't drive")


#   NOT
#   This wil flip the original result of the condition, eg. if it was true then, now its false.
if not 3 > 1:
    print("something") #Will not be printed.