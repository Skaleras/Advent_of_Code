# N stands for North
# S stands for south
# E stands for east\
# W stands for west

#Oeste es West y Este es East
#NoSe == NWSE           North and South are opposites, so are West and East


#         N
#         |
#     W------E
#         |
#         S

# L stands for Left
# R stands for right
# F stands for forward

with open('E:\code\AoC\day10\input.txt', 'r') as input:
    instructions = input.read().split('\n')

points = 'NWSE'
current_direction_X = None
current_direction_Y = instructions[0][0]
x_dist = 0
y_dist = 0
for instruction in instructions:

    if instruction[0] == 'N' or instruction[0] == 'S':
        if instruction[0] == current_direction_Y:
            y_dist+= int(instruction[1:])
        else:
            y_dist-= int(instruction[1:]) #curren_y_direction update?
            if current_direction_Y == None:
                current_direction_Y = instruction[0]
            elif y_dist < 0:
                current_direction_Y = 'W'
            else:
                pass            

    elif instruction[0] == 'W' or instruction[0] == 'E':
        if instruction[0] == current_direction_X:
            x_dist+= int(instruction[1:])
        else:
            x_dist-= int(instruction[1:])
            if current_direction_X == None:
                current_direction_X = instruction[0]
            elif x_dist < 0:
                current_direction_X = 'W'
            else:
                pass
    
    else:
        if instruction[0] == 'L':
            pass
        elif instruction[0] == 'R':
            pass
        else:
            pass