import re
data = open('E:\code\AoC\day2\passwords_data.txt', 'r')
my_input = data.read()
list_of_past_password = my_input.split('\n')
counter_of_valid_passwords = 0
for i in list_of_past_password:
    pieces = re.split('( \w: )', i)
    #print(pieces)
    limits = pieces[0].split('-')
    #print(limits)
    min_lim = int(limits[0])
    max_lim = int(limits[1])
    target_policy_letter = pieces[1].strip()[0]
    policy_counter = 0
    for j in pieces[2]:
        if j == target_policy_letter:
            policy_counter+= 1
    print(' ')
    print(pieces[2])
    if policy_counter < min_lim or policy_counter > max_lim:
        print("This password didn't pass the policy requirement\
        range of", pieces[0], 'times', target_policy_letter)
    else:
        counter_of_valid_passwords+= 1
        print("This password is ok with the policy requirement\
        range of", pieces[0], 'times', target_policy_letter)
print(' ')
print(counter_of_valid_passwords, 'valid passwords in total')