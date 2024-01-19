
print("The Love Calculator is calculating your score...")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#   Conbine the name1 and name2 so we only have a single string to check.
#   convert the combined names into lower case and make those into a new variable.
combined_names = name1 + name2
lower_names = combined_names.lower()

#   This counts how many times a letter is in both names or the string.
#   At the end, add all of those values up and store them in a new variable.
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

#   Adding these two numbers togther will make 1 whole number, we need to convert to strings.
#   Once these two numbers are a while number (2 + 5 = 25.) Convert into an integer.
score = int(str(first_digit) + str(second_digit))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
