import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_the_game = False

word_list = [
    "aardvark",
    "baboon",
    "camel",
    "dolphin",
    "elephant",
    "flamingo",
    "giraffe",
    "hippo",
    "iguana",
    "jackal",
    "kangaroo",
    "lemur",
    "meerkat",
    "narwhal",
    "orangutan",
    "penguin",
    "quokka",
    "rhino",
    "squirrel",
    "tiger",
    "uakari",
    "vulture",
    "walrus",
    "xerus",
    "yak",
    "zebra",
]
chosen_word = random.choice(word_list)

lives = 6
if lives == 0:
    end_of_the_game = True

print(f"\nPssst, the solution is {chosen_word}.\n") #! For debugging purposes.

display = []

for letter in chosen_word:
    display += "_"
print(display)



while not end_of_the_game:
    guess = input("\nGuess a letter:\n").lower()  # User inputs their guess, converts to lowercase.

    for index in range(len(chosen_word)):   # Interation over 0 to 6.
        if chosen_word[index] == guess:     # Since this will is calling each letter, == 'a' ?    
            display[index] = (guess)        # Updates the variable, the current list now updated with the guessed letters.

        elif chosen_word[index] != guess:
            lives = lives - 1
    
    
    print(f"\n{' '.join(display)}")           # Join all the elements in the list and turn it into a String.

    
    if "_" not in display:                  # Check if user has got all letters.
        end_of_the_game = True
        print("\nYou win.")





    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.


