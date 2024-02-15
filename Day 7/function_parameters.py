
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



#? Codecademy Functions.


def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
    car_rental_total = car_rental_rate * trip_time
    hotel_total = (hotel_rate * trip_time) - 10
    trip_total = car_rental_total + hotel_total + plane_ticket_price

    return trip_total

print(calculate_expenses(200, 100, 100, 5))



#? Functions with Arguments
# Default arguement >>
def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
    print("Here is what your trip will look like!")
    print(f'First, we will stop in {first_destination}, then {second_destination}, and lastly {final_destination}')

trip_planner("Brooklyn", "Queens")




#? Built-In vs User functions;

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:
max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)

min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price)

rounded_price = round(tshirt_price)
print(rounded_price)


#! Function Returns

def calculate_exchange_usd(us_dollars, exchange_rate):
  return us_dollars * exchange_rate

new_zealand_exchange = calculate_exchange_usd(100, 1.4)

print("100 dollars in US currency would give you " + str(new_zealand_exchange) + " New Zealand dollars")

int()
str()
