
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

import random


user_actions = int((input("What do you choose?\n0 for Rock\n1 for Paper\n2 for Scissors.\n")))
possible_actions = str([rock, paper, scissors])              # Define the actions in a list.
user_input = (possible_actions[user_actions])           # From the list (possible actions), pick out the indexed numbed.

computer_actions = (random.choice(possible_actions))    # CPU random choice is actioned.



if user_actions == computer_actions:
    print(f"Both players selected {user_actions}, its a tie!")

elif user_actions == "rock":
    if computer_actions == "scissors":
        print("You win!")
    else:
        print("You lose!")


elif user_actions == "paper":
    if computer_actions == "rock":
        print("You win!")
    else:
        print("You lose!")



elif user_actions == "scissors":
    if computer_actions == "paper":
        print("You win!")
    else:
        print("You lose!")