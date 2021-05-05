# Getting the data, eliminating the newlines and making a list
data = open('E:\code\AoC\day1\input.txt', 'r')
my_input = data.read()
string_numbers = my_input.split()
numbers = list()

#changing data type to integer and appending it to other list
for i in string_numbers:
    i = int(i)
    numbers.append(i) 

end = None    #Flag value to terminate loops
for number in numbers:
    for n in numbers:
        #print(n, number) Debugging
        if number + n == 2020:
            end = True
            break
    if end:
        break
print(number, n, number*n)
