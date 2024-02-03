# Part one.
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()





while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()