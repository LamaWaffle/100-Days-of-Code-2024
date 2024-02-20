
switched_on = True
while switched_on:
    print("I am a robot, i am switched on.")
    answer = input("Would you like to turn me off?\n")
    if answer == "yes":
        switched_on = False
        