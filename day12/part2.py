dirs = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
xPos, yPos = 0, 0
xWay, yWay = 10, 1
with open('E:\code\AoC\day12\input.txt') as fp:
    line = fp.readline()
    while line:
        action, value = line[0], int(line.strip()[1:])

        if action in dirs:
            dx, dy = dirs[action]
            xWay += value * dx
            yWay += value * dy
        elif action in {'L', 'R'}:
            rotation = (value if action == 'R' else 360 - value)
            if rotation == 90 or rotation == 270:
                tmp = yWay
                yWay = xWay * (-1 if rotation == 90 else 1)
                xWay = tmp * (1 if rotation == 90 else -1)
            elif rotation == 180:
                xWay *= -1
                yWay *= -1
        elif action == 'F':
            xPos += value * xWay
            yPos += value * yWay
        line = fp.readline()

print(f'\nPart 2\n{abs(xPos) + abs(yPos)}')
