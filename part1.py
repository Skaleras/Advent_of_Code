with open('E:\code\AoC\day9\input.txt', 'r') as input:
    numbers = input.read().split("\n")
#print(numbers)
dict_numbers = dict()
#print(dict_numbers)
for index , value in enumerate(numbers):
    dict_numbers[index] = value
preamble = list()
for index in list(range(25)):
    preamble.append(int(dict_numbers[index]))
end = True
index = 25
while True:
    index += 1
    for j in preamble:
        for k in preamble:
            if dict_numbers[index] == j + k:
                end = True
                break
        if end:
            break
    if not dict_numbers[index] == j + k:
        break
    preamble.append(dict_numbers[index])
    preamble.pop(0)
print(dict_numbers[index])