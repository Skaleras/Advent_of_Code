import re
with open('E:\code\AoC\day2\passwords_data.txt', 'r') as fh:
    password_list = fh.read().split('\n')

password_counter = 0
for password in password_list:
    pieces = re.split('( \w: )', password)
    #print(pieces, 'these are the pieces')

    limits = pieces[0].split('-')
    #print(limits)

    min_lim, max_lim = int(limits[0]), int(limits[1])
    target_policy_letter = pieces[1].strip()[0]
    
    policy_counter = 0
    for letter in pieces[2]:
        if letter == target_policy_letter:
            policy_counter+= 1

    #print(pieces[2])
    if policy_counter < min_lim or policy_counter > max_lim:
        pass

    else:
        password_counter+= 1

print(password_counter, 'valid passwords in total')