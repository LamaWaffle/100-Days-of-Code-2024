

# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# Simple Function
def greet():
    print("Hello human..")
    print("I am a robot.")
    print("Beep Boop.\n")

greet()


# Functions with 'positional' arguments.
def greet_with_name(name, age):
    print(f"Hello {name}.")
    print(f"Are you over {age} ?")

greet_with_name("Matthew", "21")


# Functions with 'Keyword' arguments.
def greet_with_name_2(name, age):
    print(f"Hello {name}.")
    print(f"Are you over {age} ?")

greet_with_name_2(name="Matthew", age=17)



# Functions with 'Default' arguments.
