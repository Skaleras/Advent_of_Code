with open("E:\code\AoC\day3\\trees.txt", 'r') as f:
    lines= f.readlines()
print(lines)

current_x_position = 0
movement_x_axis = 3
movement_y_axis = 1

trees_counter = 0
for current_y_position, line in enumerate(lines):
    if line[current_x_position] == "#":
        trees_counter+=1
    current_x_position=(current_x_position + movement_x_axis) % 31
   #print(current_x_position) #debugging
print("Solution 1:", trees_counter)
