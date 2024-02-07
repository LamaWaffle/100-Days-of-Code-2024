
# def add_func(x, y):
#     z = x + y
#     return z

# def subtract_func(x, y):
#     z = x - y
#     return z

# print(add_func(1, 2))       # Here we are calling the function and passing the arguments 1 and 2.



# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last

# full_name = create_name('matthew', 'eberhard')
# print(full_name)



# def create_name(first, last):
#     first = len(first)
#     last = len(last)
#     return first + last

# full_name = create_name('matthew', 'eberhard')
# print(full_name)


# def greeting(name, age):
#     print(f"Hi {name}")
#     print(f"You are {age} years old.")


# greeting('Matthew', 24)


def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Matty")

print(message)