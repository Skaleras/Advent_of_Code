with open('E:\code\AoC\day10\input3.txt', 'r') as input:
    adapters = list(map(int, input.read().strip().split('\n')))
adapters.sort()
print(adapters)
print(len(adapters))
print(' ')

initial_outlet = 1
original_len = len(adapters)
sorted_lists = list()
counter_1 = 0
for index, adapter in enumerate(adapters):
    if adapter == 1:
        counter_1+=1
    elif adapter - adapters[index-1] == 1:
        counter_1+=1

counter_2 = 0
for index, adapter in enumerate(adapters):
    if index == len(adapters)-2:
        break
    if adapters[index+2] - adapter == 2:
        counter_2+=1

counter_3 = 0
for index, adapter in enumerate(adapters):
    if index == len(adapters)-1:
        break
    if adapters[index+1]- adapter == 3:
        counter_3+=1
print(counter_1*counter_2*counter_3+initial_outlet)
# adding the diffences that are one between adjacent index plus the initial 
# and final connection adds up to 8
# testing with the other inputs
# dynamic programming problem
