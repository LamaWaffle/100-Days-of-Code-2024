database = [
    {
        "Accounts": {
            "uuid-1234": {
                "Username": "matty.eberhard@gmail.com",
                "Password": "password123",
            },
            "uuid-2727": {
                "Username": "jsmith@gmail.com",
                "Password": "pass1234444",
            },
            "uuid-8888": {
                "Username": "marry@husman.com",
                "Password": "dogcutelol",
            },
        }
    }
]

def add_user(uuid, username, password, name):
    new_user = {}
    new_user["uuid"] = uuid
    new_user["Username"] = username
    new_user["Password"] = password
    new_user["Name"] = name

    database.append(new_user)



running = True
while running:

    uuid = input("\n What is the new users uuid? \n")
    username = input("What is the new users username? \n")
    password = input("What is the new users password? \n")
    name = input("What is thier name? \n")

    add_user(uuid, username, password, name)

    print_all = input("Would you like to print out a full list of the users? \n")
    if print_all == 'yes':
        for users in database:
            print(users)

    restart = input("Would you like to add another user into the database? \n")
    if restart == "no":
        print("Goodbye for now..")
        running = False
