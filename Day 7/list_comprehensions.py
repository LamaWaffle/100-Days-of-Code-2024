
#* Example formatting below.
new_list = [<expression> for <element> in <collection>]


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
