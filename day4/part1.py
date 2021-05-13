import re
data = open('E:\code\AoC\day4\input.bat', 'r')
my_input = data.read()
#print(my_input)
pattern = '\n\n'
documents = re.split(pattern, my_input)
data_checklist = ['ecl','pid','eyr','hcl','byr', 'iyr', 'hgt', 'cid']
ok_passport_counter = 0
for document in documents:
    print(document)
    print('____________________')
    data_counter=0
    for data in data_checklist:
        if data in document:
            data_counter+=1
            if data_counter==7 and 'cid' not in data:
                ok_passport_counter+=1
#            if data_counter==8:
#                ok_passport_counter 
    print('passport that passed are', ok_passport_counter,\
        'and there were', data_counter, 'items in this passport')
    print('____________________')
print(ok_passport_counter)
