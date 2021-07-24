# N stands for North
# S stands for south
# E stands for east
# W stands for west

#Oeste es West y Este es East
#NoSe == NWSE           North and South are opposites, so are West and East


#         N
#         |
#     W---+--E
#         |
#         S

# L stands for Left
# R stands for right
# F stands for forward

with open('E:\code\AoC\day12\input.txt', 'r') as input:
    instructions = input.read().split('\n')

def degrees_to_position(degrees, action):
    #degrees have to be integers and action has to be string L or R
    if degrees == 90:
        if action == 'L':
            return 1
        else:
            return -1
    elif degrees == 180:
            return 2
    else:           # the last case is when it's 270 degrees
        if action == 'L':
            return 3
        else:
            return -3

points = 'NWSENWSENWSE'
facing_direction = 'E'
x_dist_positive, y_dist_positive = 0, 0
x_dist_negative, y_dist_negative = 0, 0
for instruction in instructions:

    boat_action = instruction[0]
    value_action = int(instruction[1:])
    if boat_action == 'N' or boat_action == 'S':
        if boat_action == 'N':
            y_dist_positive+= value_action
        else:
            y_dist_negative+= value_action

    elif boat_action == 'W' or boat_action == 'E':
        if boat_action == 'E':
            x_dist_positive+= value_action
        else:
            x_dist_negative+= value_action
    
    elif boat_action == 'L' or boat_action == 'R':
        position_index = 0
        position_index = degrees_to_position(value_action, boat_action) + points.index(facing_direction)
        facing_direction = points[position_index]

    else:
        if facing_direction == 'N':
            y_dist_positive+= value_action
        elif facing_direction == 'S':
            y_dist_negative+= value_action
        elif facing_direction == 'E':
            x_dist_positive+= value_action
        elif facing_direction== 'W':
            x_dist_negative+= value_action

print((x_dist_positive-x_dist_negative)+(y_dist_positive-y_dist_negative))
