
print("Thank you for choosing Python Pizza Deliveries!")

size = input("Size? s, m or l ? \n") 
add_pepperoni = input("Pepproni? y or n\n") 
extra_cheese = input("Extra cheese? y or n\n") 

bill = 0

# Checks the string value to charge size.
if size == "s":
    bill += 15

elif size == "m":
    bill += 20

else:
    bill += 25


# Charges $2 for pepperoni, $3 for large.
if add_pepperoni == "y":
    if size == "S":
        bill += 2
    else:
        bill += 3


# Charges for extra cheese with any order options.
if extra_cheese == "y":
    bill += 1


print(f"Your final bill is: ${bill}.")
