### This is the problem description
# Each policy actually describes two positions in the password, 
# where 1 means the first character,
# 2 means the second character, and so on. 
# (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
# Exactly one of these positions must contain the given letter. 
# Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

import re
data = open('E:\code\AoC\day2\passwords_data.txt', 'r')
my_input = data.read()
list_of_past_password = my_input.split('\n')
counter_of_valid_passwords = 0
for i in list_of_past_password:
    pieces = re.split('( \w: )', i)
    #print(pieces)
    limits = pieces[0].split('-')
    target_policy_letter = pieces[1].strip()[0]
    #print('the policy letter',target_policy_letter,'must be in the position', limits[0],'or', limits[1], 'only once!')
    min_lim = int(limits[0])
    max_lim = int(limits[1])
    #print(target_policy_letter)
    if target_policy_letter== pieces[2][min_lim-1] and target_policy_letter == pieces[2][max_lim-1]:
        print('Invalid password', pieces[2])
    if target_policy_letter != pieces[2][min_lim-1] and target_policy_letter != pieces[2][max_lim-1]:
        print('Invalid password', pieces[2])
    if target_policy_letter == pieces[2][min_lim-1] and target_policy_letter != pieces[2][max_lim-1]:
        print('Valid password', pieces[2])
        counter_of_valid_passwords+= 1
    if target_policy_letter != pieces[2][min_lim-1] and target_policy_letter == pieces[2][max_lim-1]:
        print('Valid password', pieces[2])
        counter_of_valid_passwords+= 1
    print(' ')
print(' ')
print('There are',counter_of_valid_passwords, 'valid passwords, acording to the policies')
    
    