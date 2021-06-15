with open('E:\code\AoC\day9\input.txt', 'r') as input:
    numbers = list(map(int, input.read().split("\n")))
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

    preamble.append(dict_numbers[index])
    preamble.pop(0)
    if not last_valid_number:
        invalid_number = last_number
        break

#print(invalid_number)
#print(invalid_number, len(str(invalid_number)), 'the index is', index)
for length in range(2, 1000+1):
    for offset in range(1000-length+1):
        contiguous_set = numbers[offset:offset+length]
        if sum(contiguous_set) == invalid_number:
            #print('the contiguous_set starts at index', offset, 'and ends at index', offset+length)
            #print(contiguous_set)
            print(min(contiguous_set) + max(contiguous_set))