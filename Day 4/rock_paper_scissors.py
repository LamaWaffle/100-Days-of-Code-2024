
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

user_choice = int((input("What do you choose?\n0 for Rock, 1 for Paper, 2 for Scissors.\n")))
possible_actions = [rock, paper, scissors]                      # Define the actions in a list.
users_actions = (possible_actions[user_choice])                 # From the list (possible actions), pick out the indexed number that the user chose.

computer_actions = (random.choice(possible_actions))            # CPU random choice is actioned.


if users_actions == computer_actions:
    print(users_actions)
    print(f"Computer chose: {computer_actions}")
    print("Its a tie!")

elif users_actions == rock:
    if computer_actions == scissors:
        print(users_actions)
        print(f"Computer chose: {computer_actions}")
        print("You win!")
    else:
        print(users_actions)
        print(f"Computer chose: {computer_actions}")
        print(computer_actions)


elif users_actions == paper:
    if computer_actions == rock:
        print(users_actions)
        print(f"Computer chose: {computer_actions}")
        print("You win!")
    else:
        print(users_actions)
        print(f"Computer chose: {computer_actions}")
        print("You Lose!")


elif users_actions == scissors:
    if computer_actions == paper:
        print(users_actions)
        print(f"Computer chose: {computer_actions}")
        print("You win!")
    else:
        print(users_actions)
        print(f"Computer chose: {computer_actions}")
        print("You Lose!")



