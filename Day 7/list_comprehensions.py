
#* Example formatting below.
# new_list = [<expression> for <element> in <collection>]
# new_list = [new_item for item in list]


numbers = [2, -1, 79, 33, -45]
doubled = []

for number in numbers:
  doubled.append(number * 2)
print(doubled)



numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]  # Same example above, but as a list comprehension.
print(doubled)



numbers = [12, 99, 100]
even = [int for int in numbers if int % 2 == 0]



fruits = ['apple', 'banana', 'orange', 'pear', 'kiwi', 'apple', 'banana']
edible = [print(fruit) for fruit in fruits ]


bits = [False, True, False, False, True, False]
new_bits = [1 if bits == True else 0 in bits]

for b in bits:
    if b == True:
        new_bits.append(1)
    else:
        new_bits.append(0)




numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []

for num in numbers:
  if num < 0: 
    only_negative_doubled.append(num * 2)

only_negative_doubled = [num * 2 for num in numbers if num < 0]



numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]
print(doubled)



heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)






# Codecademy Loop exercise:

single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []

for digit in single_digits:
    print(digit)
    squares.append(digit * digit)
print(squares)

cubes = [digit ** 3 for digit in single_digits]
print(cubes)



# Comprehension list of the example above.

single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [digit * digit for digit in single_digits]
cubes = [digit ** 3 for digit in single_digits]

print(squares, cubes)





# List comprehensions exercises.

words = ["cat", "window", "defenestrate", "python", "list", "comprehension", "example"]
big_words = [word for word in words if len(word) > 4 ]
print(big_words)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)


numbers = [1, 2, 3, 10, 11, 12, 13, 14, 15]
squared = [num*num for num in numbers if num <= 10]
print(squared)

numbers = [3, 4, 9, 11, 18, 20, 21, 25, 27]
div_by_3 = [num for num in numbers if num / 3]
print(div_by_3)
