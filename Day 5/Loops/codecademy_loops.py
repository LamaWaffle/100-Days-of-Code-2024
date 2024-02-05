
#! For loops
board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

for game in board_games: print(game)

for number in range(5):
    print("This is number " + str(number + 1))
          

#! While loops
count = 0 
while count <= 3:
    count += 1
    print(count)

countdown = 10
while countdown >= 0: print(countdown); countdown -= 1
print('Blastoff!')


#! While loops with Lists.
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)     # Here we get the total length of the list.
index = 0                       # Here we set the starting index to 0. Compare to this.

while index < length:           # Here we check if the index is less than the length of the list.
  print(f'I am learning about {python_topics[index]}') # Here we print the current item in the list.
  index += 1

#? An alternative way to do this is to use the for loop.
while index < length: print(f'I am learning about {python_topics[index]}'); index += 1

#! Loop Breaks
# Loops breaks once reach the desired output, exits the loop.

items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]

for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break  # Instead of the loop continuing to interate, it breaks at knit dress.

print("End of search!")


#? Can also be included with if / else statements.
while counter < 10:
    counter += 1
    if randint(1,11) == 11:
        print ('Won!')
        break
else:
	print ('done')
# Won!
    

#! Loop Continues
# Loop continues once reach the desired output, exits the loop.
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for int in ages:
  if int < 18:  # if 12 is < 18 (True), skip. Otherwise, print integer.
    continue
  print(int)
