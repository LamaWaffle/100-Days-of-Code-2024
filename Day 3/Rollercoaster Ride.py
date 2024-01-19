
print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
    print("You are tall enough, please enjoy your ride!\n")
    age = int(input("What is your age?\n"))


    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    
    elif age < 18:
        print("Youth tickets are $7.")
        bill = 7

    elif age >= 45 and age <= 55:     # Here we are catching the midlife crisis window.
        print("You can enjoy the ride for free!")
        bill = 0

    else:
        print("Adult tickets are $12.")
        bill = 12


    photo = input("Do you want a photo taken? Y or N. ")
    if photo == "y":
        bill += 3 # Same as 'bill = bill + 3'


    print(f"Your final bill is ${bill}.")

else:
    print("You are too short! Goodbye.")


