must_be_in = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
with open('E:\code\AoC\day4\input.bat', 'r') as input:
    passports = input.read().split('\n\n')
    passports = [passport.replace('\n', ' ') for passport in passports]

def good_passport(passport, counter=0):
    if all(x in passport for x in must_be_in):
        return counter+1
    else:
        return 0

answer = map(good_passport, passports)
print(sum(answer))