import random


random_int = random.random()  # Generates a random integer.
random_float = random.randint(0, 5)  # Generates a random float (decimal number).

mix = random_float * random_int  # Can multiply the float and integers.
print(mix)

# Random numbers are great for creating dice, flipping coins etc.

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# Heads of Tails
print("Heads" if random.randint(0, 1) else "Tails")

# Heads of Tails - alternative.
result = random.randint(0, 1)
print("Heads" if result == 1 else "Tails")

# Heads of Tails - normal.
result = random.randint(0, 1)
if result == 1:
    print("Heads Nat YOLO Queen has been here")
else:
    print("Tails Nat YOLO Queen has been here")
