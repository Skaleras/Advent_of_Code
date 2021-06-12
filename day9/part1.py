with open('E:\code\AoC\day9\input.txt', 'r') as input:
    numbers = list(map(int, input.read().split("\n")))
#The bug was in the line just above, all the numbers were still strings 
#when I populated the dictionary of numbers

#print(numbers)

dict_numbers = dict()
for index , value in enumerate(numbers):
    dict_numbers[index] = value
    
preamble = list()
for index in list(range(25)):
    preamble.append(dict_numbers[index])
    
index = 24
while True:
    index += 1
    last_number = dict_numbers[index]
    last_valid_number = False
    for inner in preamble:
        for outer in preamble:
            if inner + outer == last_number:
                last_valid_number = True

    if not last_valid_number:
        last_invalid_number = last_number
        break
    preamble.append(dict_numbers[index])
    preamble.pop(0)

print(last_invalid_number)
