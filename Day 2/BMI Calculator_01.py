
str_height = input("What is your height? ")
# 2nd input: enter weight in kilograms e.g: 72
str_weight = input("What is your weight? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

int_weight = int(str_weight)
float_height = float(str_height)

bmi = str(int_weight / float_height)

print("Your BMI is " + bmi)