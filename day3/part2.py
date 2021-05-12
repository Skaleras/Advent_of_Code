with open("E:\code\AoC\day3\\trees.txt", 'r') as f:
    lines= f.readlines()
list_of_slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
# The first term of the tuple is the run and the second term is the rise
# we are more interested in getting faster at the bottom not faster to the sides
# so let's sort the list descendly by the rise term and descending for the run to avoid 
# unnecesary trees in the first runs

list_of_slopes.sort(key=lambda x:x[1], reverse=True)
#print(list_of_slopes, 'sorted')
list_of_trees_counter = list()
for slope in list_of_slopes:
    print('slope:', slope)
    movement_x_axis, movement_y_axis= slope[0],slope[1]
    current_x_position = 0
    trees_counter = 0
    for (current_y_position, line) in enumerate(lines):
        if current_y_position % movement_y_axis == 0:
            
            if line[current_x_position] == "#":
                trees_counter+=1
            current_x_position=(current_x_position + movement_x_axis) % 31
    print('trees with this slope:', trees_counter)
    list_of_trees_counter.append(trees_counter)
    print('____________')
solution = list_of_trees_counter[0]*list_of_trees_counter[1]*list_of_trees_counter[2]\
*list_of_trees_counter[3]*list_of_trees_counter[4]

print('The solution is', solution)
##print("Solution 2:", trees_counter)