
# # Write your code below this line 👇
# import math

# def paint_calc(height, width, cover):
#     number_of_cans = (height * width) / cover
#     cans = int(math.ceil(number_of_cans))
#     print(f"You'll need {cans} cans of paint.")
    
# # Write your code above this line 👆
# # Define a function called paint_calc() so the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input()) # Height of wall (m)
# test_w = int(input()) # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)





# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime == True:
        print("It's a prime number.")       
    else:
        print("It's not a prime number.")


# Write your code above this line 👆
    
#Do NOT change any of the code below👇
# n = int(input()) # Check this number
prime_checker(number=13)