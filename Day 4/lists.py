numbers = [1, 2]  # List of integers
list = ["flowers", "pot_plants"]  # List of string values.

states_of_america = [
    "Delaware",
    "Pennsylvania",
    "Texas",
]  # Lists also have order, these are in ORDER.

print(states_of_america[1])

states_of_america[2] = "yeehaaw"
print(states_of_america[-1])

states_of_america.append("New State York")
print(states_of_america)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

vegetables.sort()
print(vegetables)
