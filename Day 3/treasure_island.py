print(
    """  
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
"""
)

print("Welcome to Treasure Island!\n\nYour mission is to find the hidden treasure.")

choice1 = input("First decision, are you going to go left or right?\n".lower())
if choice1 == "left":
    print("You walk through the wet swamp filled with trout.\n")

    choice2 = input(
        "You see a lake in front of you, should you wait or swim into it?\n".lower()
    )
    if choice2 == "wait":
        choice3 = input(
            "Well done.\nA magical corridoor filled with doors appear in front of you.\nDo you take the Red, Blue or Yellow door?\n".lower()
        )
        if choice3 == "yellow":
            print("You have won the game!!")
        elif choice3 == "red":
            print("You are burned to death by a flaming fireball!")

        elif choice3 == "blue":
            print("A Hippogriff eats you in one bite!")

        else:
            print("GAME OVER!")

    else:
        print("You are attacked by a huge crocodile!")
else:
    print("You fall into a hole and die a horrible death. RIP.")
