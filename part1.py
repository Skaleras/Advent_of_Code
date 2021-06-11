with open('E:\code\AoC\day9\input.txt', 'r') as input:
    numbers = input.read().split("\n")

dict_numbers = dict()
for index , value in enumerate(numbers):
    dict_numbers[index] = value
    
preamble = list()
for index in list(range(25)):
    preamble.append(int(dict_numbers[index]))
    
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
        print(last_invalid_number)
    preamble.append(dict_numbers[index])
    preamble.pop(0)
    #print(preamble)
