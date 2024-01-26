
# Fizz Buzz game.

user_choice = int(input("Pick a number from 1 to 100. "))
    
for number in range(1, user_choice + 1):
    
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 5 == 0:
        print("Buzz")

    elif number % 3 == 0:
        print("Fizz")

    else:
        print(number)

