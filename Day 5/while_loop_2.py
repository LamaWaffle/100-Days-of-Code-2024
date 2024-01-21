
password = input("Enter your password: \n")

while password != "abc123":           # This essentially checks if the password is correct or not.
    password = input("Incorrect - Enter your password: \n")

print("Password was correct!")
