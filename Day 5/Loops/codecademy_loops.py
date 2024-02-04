
#! For loops
board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

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

