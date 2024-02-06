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
