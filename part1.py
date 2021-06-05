with open('E:\code\AoC\day8\input.txt', 'r') as input:
    instructions = input.read().split("\n")
#print(instructions)
accumulator = 0
operation_dict ={}
for index , operation in enumerate(instructions):
    #print(index, operation)
    operation_dict[index] = operation.split()
    operation_dict[index].append(0)
    
# I like the data structure so far, I added the 0 in the list inside the dictionary 
# so I can change it if the loops falls back into that operation while also always knowing
# in which index I am with the enumerate function
# it has the form >>>    index_of_operation : [operation, argument, loop_breaker]

index = 0
while True:
    if operation_dict[index][0] == 'acc':
        if operation_dict[index][2] == 1:
            break
        accumulator = accumulator + int(operation_dict[index][1])
        operation_dict[index].pop()
        operation_dict[index].append(1)
        index = index + 1
        
    elif operation_dict[index][0] == 'jmp':
        if operation_dict[index][2] == 1:
            break
        operation_dict[index].pop()
        operation_dict[index].append(1)
        index = index + int(operation_dict[index][1])
    else:
        index = index + 1

print(accumulator)


    
    
    
