
def display_invoice(username, amount, due_date):
    print(f"Hellow {username}!")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Matthew", 42.50, "01/09/2025")





def max_of_two_nums(x, y):
    if x > y:
        return x
    else:
        return y

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = max_of_two_nums(num1, num2)

print("The highest number is:", result)


#* 2. Write a Python function to sum all the numbers in a list.
#* Sample List : (8, 2, 3, 0, 7)
#* Expected Output : 20 

def sum_all(num):
    total = 0
    for x in num:
        total += x
    return total

print(sum_all((8, 2, 3, 0, 7)))


#* 3. Write a Python function to multiply all the numbers in a list.
#* Sample List : (8, 2, 3, -1, 7)
#* Expected Output : -336 

def multiply_all(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

print(multiply_all((8, 2, 3, -1, 7)))


#* 4. Write a Python program to reverse a string.
#* Sample String : "1234abcd"
#* Expected Output : "dcba4321"

def string_reversed(str1):
    rstr1 = ''
    index = len(str1)
    while index > 0
        
