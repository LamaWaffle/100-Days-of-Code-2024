
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for steps in range(6):  # This is a for loop that runs 6 times.
    jump()

# This can also be achieved by using `while` loops.
    
num_of_hurdles = 6
while num_of_hurdles > 0:
    jump()
    num_of_hurdles -= 1
    print(num_of_hurdles)


while at_goal() != True:
    jump()

# Another way to write this, is using a negation.

while not at_goal():
    print('hello')




def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    if wall_on_right():
        move()
    else:
        turn_right()    
    
    turn_right()
    move()
    turn_right()
    move()
    if wall_on_left():
        move()
    else:         
        turn_left()




while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()



def jump():
    if wall_in_front():
        turn_left()
    turn_left()
    move()
    while wall_on_right() and front_is_clear():
        move()

    else:
        turn_right()
        move()
        turn_right()
        move() # Might need to remove.


while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()

        