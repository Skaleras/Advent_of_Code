from typing import Counter


r = open('E:\code\AoC\day6\input.txt').read().strip('\n')
input = r.split('\n\n')

#Part 2:
count = 0
#counter_2 = 0
for group in input:
    #print('___________________________')
    #counter_2+=1
    group = group.splitlines()    # https://www.tutorialspoint.com/python3/string_splitlines.htm
    #print('this is the group:', group)
    ans = set(group[0])           # https://www.w3schools.com/python/python_sets.asp
    #print('this is the set:', ans)
    #print('____________________________')
    for person in group:
        ans = ans & set(person)         # https://www.youtube.com/watch?v=5J4rWJHwLSE
        #print('this is an extended set:', ans)
    count = count + len(ans)
    #if counter_2 == 15:
    #    break

print(count)