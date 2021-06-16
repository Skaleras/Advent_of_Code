with open('E:\code\AoC\day10\input.txt', 'r') as input:
    adapters = list(map(int, input.read().strip().split('\n')))
adapters.sort()
#print(adapters)

counter_1 = 0
counter_3 = 1   #the highest always has +3 jolt diference
for index, adapter in enumerate(adapters):
    if adapter == 1:
        counter_1+=1
    elif adapter - adapters[index-1] == 1:
        counter_1+=1
    else:
        counter_3+=1

print('the result is:', counter_1*counter_3)