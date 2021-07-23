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

with open('E:\code\AoC\day10\input.txt', 'r') as input:
    instructions = input.read().split('\n')

points = 'NWSENWSENWSE'
facing_direction = 'E'
x_dist = 0
y_dist = 0
for instruction in instructions:
    if instruction[0] == 'N' or instruction[0] == 'S':
        if instruction[0] == facing_direction:
            y_dist+= int(instruction[1:])
        else:
            y_dist-= int(instruction[1:])
            if y_dist < 0:
                y_dist = y_dist*(-1)  

    elif instruction[0] == 'W' or instruction[0] == 'E':
        if instruction[0] == facing_direction:
            x_dist+= int(instruction[1:])
        else:
            x_dist-= int(instruction[1:])
            if x_dist < 0:
                x_dist = x_dist*(-1)
    
    elif instruction[0] == 'L' or instruction[0] == 'R':
        position_index = 0
        position_index = degrees_to_position(int(instruction[1:]), instruction[0]) + points.index(facing_direction)
        facing_direction = points[position_index]

    else:
        if facing_direction == 'N':
            x_dist+= int(instruction[1:])
        elif facing_direction == 'S':
            pass
