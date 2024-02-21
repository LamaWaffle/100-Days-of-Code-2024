
import random
from sty import fg

# def my_function():
#     result = 3 * 2
#     return result

# output = my_function()      # The output is 6, places it in a new variable.




def format_name(f_name, l_name):      # Takes first and last name into title case.
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"

print(format_name("matthew", "EBERhARD"))


def add_numbers(a, b):
    return a + b

result = add_numbers(17, 77)
print(result)




def about_me(name, profession, pet):
    print(f"Hi my name is", name)
    print(f"i am a", profession)
    print(f"and i have a", pet)

about_me("Matthew", "Coder", "Dog")




def generate_RGB():
    red = random.randint(0, 256)
    green = random.randint(0, 256)
    blue = random.randint(0, 256)
    return red, green, blue


def generate_colour(red, green, blue):
    return fg(red, green, blue)


red, green, blue = generate_RGB()
colour = generate_colour(red, green, blue)

print(colour, "Im randomly changing colours!")
