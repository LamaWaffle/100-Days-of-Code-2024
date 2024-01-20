
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?\n") 
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# Letter logic.
letter = position[0].lower()      # Seperate the first letter of the input and converts to lowercase, asigns it a new variable.

abc = ["a", "b", "c"]                   # Creates a new list of abc's - used to compare with.
letter_index = abc.index(letter)        # Here we compare the abc list and find the index of the input (position).

# Number logic.
number_index = int(position[1]) -1      # Convert the position input into an Int, gather its position.
map[number_index][letter_index] = 'X'   # Specifies the indexed value, then adds and 'X' to it.


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
