# Example.
water_level = 50
if water_level > 80:
    print(f"Drain water - water is at {water_level}")

else:
    print(f"Keep filling up - water is at {water_level}")


# Rollercoaster.
print("Welcome to the Rollercoaster!")
height = int(input("What is your height?\n"))

if height > 120:
    print("You can ride on this Rollercoaster!")

else:
    print("You are too short, sorry buddy :(")


# Odd or even.
number = int(input("Choose your number:\n"))

if number % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")