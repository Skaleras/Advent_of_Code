instructions = [[line.strip()[0], int(line.strip()[1:])] 
                for line in open('E:\code\AoC\day12\input.txt', 'r')]

waypoint = {'N': 1, 'W': 0, 'S': 0, 'E': 10}
ship_position = {'N': 1, 'W': 0, 'S': 0, 'E': 10}
directions = 'NWSE'
#print(instructions)

def move_to_waypoint(mult: int, s: dict, w: dict):
    for k,v in w.items():
        s[k] += mult*v
    return s

def turn_way_point(turn: str, angle: int, w: dict):
    dirs = ''.join(list(waypoint.keys()))
    if turn == 'L':
        return {(dirs[-angle//90:]+dirs[:-angle//90])[i] : \
        list(waypoint.values())[i] for i in range(len(dirs))}
    if turn == 'R':
        return {(dirs[angle//90:]+dirs[:angle//90])[i] : \
        list(waypoint.values())[i] for i in range(len(dirs))}

for instruction in instructions:
    if instruction[0] == 'F':
        ship_position = move_to_waypoint(instruction[1], ship_position, waypoint)
    elif instruction[0] == 'R' or instruction[0] == 'L':
        waypoint = turn_way_point(instruction[0], instruction[1], waypoint)
    else:
        waypoint[instruction[0]] += instruction[1]

print(abs(ship_position['N'] - ship_position['S']) + abs(ship_position['E'] - ship_position['W']))