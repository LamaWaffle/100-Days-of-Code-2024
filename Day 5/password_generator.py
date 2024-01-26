
# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

password_list = []

for _ in range(0, nr_letters):
    rando_letters = random.randint(0, len(letters) -1 )
    password_list.append(letters[rando_letters])


for _ in range(0, nr_numbers):
    rando_numbers = random.randint(0, len(numbers) - 1)
    password_list.append(numbers[rando_numbers])
                         

for _ in range (0, nr_symbols):
    rando_symbols = random.randint(0, len(symbols) - 1)
    password_list.append(symbols[rando_symbols])

password = ""
random.shuffle(password_list)

for x in password_list:
    password = password + x         

print (f"Your new password is: \n{password}")

