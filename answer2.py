# The Elves in accounting are thankful for your help; 
# one of them even offers you a starfish coin they had left over from a past vacation. 
# They offer you a second one 
# if you can find three numbers in your expense report that meet the same criteria.
data = open('E:\code\AoC\day1\input.txt', 'r')
my_input = data.read()
string_numbers = my_input.split()

four_digit_numbers = list()
three_digit_numbers = list()
two_digits_numbers = list()

for number in string_numbers:
    if len(number)== 4:
        number = int(number)
        four_digit_numbers.append(number)
    elif len(number)== 3:
        number = int(number)
        three_digit_numbers.append(number)
    elif len(number)==2:
        number = int(number)
        two_digits_numbers.append(number)
two_digits_numbers.sort()
three_digit_numbers.sort()
four_digit_numbers.sort()


end = False
for i in two_digits_numbers:
    for j in three_digit_numbers:
        for k in four_digit_numbers:
            if i + j + k == 2020:
                end = True
                break
        if end: break
    if end: break
print(i, j, k)
print(i*j*k)