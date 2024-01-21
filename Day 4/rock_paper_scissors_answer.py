import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]  # This is putting the images into a list.

# User logic
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))  # Collect
# users input, convert to an integer, prints action.
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number - GAME OVER!")  # This is a catch in-case the users input was invalid.
    # If the result is invalid, it ends the game.

else:
    print(game_images[user_choice])

    # Computer logic
    computer_choice = random.randint(0, 2)  # Generate a random number from 0, 1 and 2, assign
    # it to computers_choice.
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:  # This is an override - were making an exception here.
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")

    elif user_choice > computer_choice:  # These are the general rules, 2 beats 0.
        print("You win!")
    elif computer_choice > user_choice:
        print("You lose.")

    elif computer_choice == user_choice:  # A catch for the draw outcome.
        print("Its a draw!")
