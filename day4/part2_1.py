import re
data = open('E:\code\AoC\day4\input.bat', 'r')
my_input = data.read()
#Regex patterns
ecl_pattern = 'ecl:(\w{3})'
pid_pattern = 'pid:(\d{9})'
eyr_pattern = 'eyr:(\d{4})'
hcl_pattern = 'hcl:(#[a-f0-9]{6})'
byr_pattern = 'byr:(\d{4})'
iyr_pattern = 'iyr:(\d{4})'
hgt_pattern = 'hgt:(\d{2,4})([a-z]{2})'
#Regexes lists
byr_list=re.findall(byr_pattern, my_input)
iyr_list=re.findall(iyr_pattern, my_input)
eyr_list=re.findall(eyr_pattern, my_input)
hgt_list=re.findall(hgt_pattern, my_input)
hcl_list=re.findall(hcl_pattern, my_input)
ecl_list=re.findall(ecl_pattern, my_input)
pid_list=re.findall(pid_pattern, my_input)
print(hgt_list)
#valid passport counter
"""valid_passport_counter = 0
mother_list = [byr_list, iyr_list, eyr_list, hgt_list, hcl_list, ecl_list, pid_list]
for son_list in mother_list:
    passport_data = list()
    passport_data.append(son_list[-1])
    son_list.pop()
    if int(passport_data[0]) in list(range(1920,2003)):
        pass
    if int(passport_data[1]) in list(range(2010,2021)):
        pass
    if int(passport_data[2]) in list(range(2020,2031)):
        pass
    if passport_data[3][-2:0] == 'in' or passport_data[3][-2:0] == 'cm':
        if passport_data[3][-2:0]
    if
    if
    if
    
    
"""