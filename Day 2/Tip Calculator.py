# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# Write your code below this line 👇

print('Welcome to the Tip Calculator!')

bill = int(input('What was the total bill? \n$'))
tip = float(input('How much tip would you like to give? \n$'))
people = int(input('How many people to split the bill? \n'))

bill_tip = bill + tip
total = round(bill_tip / people, 2)

print(F'Each person should pay: ${total}')
