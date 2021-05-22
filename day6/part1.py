import re
data = open('E:\code\AoC\day6\input.txt', 'r')
my_input = data.read()
groups_list = list()
letter_list = list()
groups = re.split('\n\n', my_input)
sums = list()

for group in groups:
    group = group.split('\n')
    groups_list.append(group)
    
counter = 0
for answers in groups_list:
    if len(answers)>1:
        sums.append(yes_counter)
        letter_list.clear()
        yes_counter = 0
        for answer in answers:
            for letter in answer:
                if letter not in letter_list:
                    letter_list.append('letter')
                    yes_counter+=1
    else:
        sums.append(yes_counter)
        letter_list.clear()
        yes_counter = 0
        for letter in answer:
            if letter not in letter_list:
                letter_list.append('letter')
                yes_counter+=1
print(sum(sums))
