r = open('E:\code\AoC\day6\input.txt').read().strip('\n')
input = r.split('\n\n')

#Part 1:
count = 0
for group in input:
    for question in 'qwertyuiopasdfghjklzxcvbnm':
        if question in group:
            count = count + 1

print(count)
