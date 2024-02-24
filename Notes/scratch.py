# switched_on = True
# while switched_on:
#     print("I am a robot, i am switched on.")
#     answer = input("Would you like to turn me off?\n")
#     if answer == "yes":
#         switched_on = False


profile = {"username:", "matthew", "password:", "1234"}

user_input = {
    "username:",
    "matthew",
    "password:",
    "1234",
    "email:",
    "matty.eberhard@gmail.com",
}

profile |= user_input
profile.update(user_input)


def counter():
    for i in range (10):
        i += 1
        print(i)
counter()


character_profile = {
    "name": "Adventurer Alex",
    "level": "12",
    "inventory":
        {"gold": 120,
         "health Potion": 2,}
}

treasure_chest = {
    "gold": 430,
    "magic sword": 1,
    "health potion": 1,
}

character_profile = character_profile | treasure_chest
print(character_profile)




