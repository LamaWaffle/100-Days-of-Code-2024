#Step 1

import random

# Step 1
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)


print(f'Pssst, the solution is {chosen_word}.')     #Testing code - helps debugging.

guess = input("Guess a letter:\n").lower()   # User inputs their guess, converts to lowercase.

for letter in chosen_word:                          # Giving a category, if the letter matches the guess.. do this or that.
    if letter == guess:                      # Comparing if the letter is equal to the guess.
        print("Right")
    else:
        print("Wrong")


