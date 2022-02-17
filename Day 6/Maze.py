# Run with Reeborg's World Maze World problem
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def follow_wall():
    if wall_in_front() == True:
        if wall_on_right() == True:
            turn_left()
        else:
            turn_right()
            move()
    elif wall_on_right() != True:
        turn_right()
        move()
    else:
        move()
    
while at_goal() != True:
        follow_wall()