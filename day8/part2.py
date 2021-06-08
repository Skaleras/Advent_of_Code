with open('E:\code\AoC\day8\input.txt', 'r') as input:
    instructions = input.read().split("\n")
#print(instructions)
accumulator = 0
operation_dict ={}
counter_1 = 0
counter_2 = 0
counter_3 = 0
for index , operation in enumerate(instructions):
    print(index, operation)
    operation_dict[index] = operation.split()
    operation_dict[index].append(0)
    if operation_dict[index][0] == 'acc':
        counter_1 += 1
    elif operation_dict[index][0] == 'jmp':
        counter_2 += 1
    else:
        counter_3 += 1
print(' ')
print('the counters are:',counter_1, counter_2, counter_3)
print(' ')
    
# I like the data structure so far, I added the 0 in the list inside the dictionary 
# so I can change it if the loops falls back into that operation while also always knowing
# in which index I am with the enumerate function
# it has the form >>>    index_of_operation : [operation, argument, loop_breaker]

#419
index = 0
while True:
    if index == 610:
        break
    #elif index == 608:
    elif operation_dict[index][0] == 'acc':
        print(index)
        if operation_dict[index][2] == 1:
            break
        accumulator = accumulator + int(operation_dict[index][1])
        operation_dict[index].pop()
        operation_dict[index].append(1)
        index = index + 1
        
    elif operation_dict[index][0] == 'jmp':
        #if index == 419:
        #    index = index + 1
        print(index, operation_dict[index][0], operation_dict[index][1])
        if operation_dict[index][2] == 1:
            break
        operation_dict[index].pop()
        operation_dict[index].append(1)
        index = index + int(operation_dict[index][1]) 
    else:
        print(index, operation_dict[index][0], operation_dict[index][1])
        index = index + 1

print(accumulator)