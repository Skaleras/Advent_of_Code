from math import prod
from itertools import combinations

with open('E:\code\AoC\day1\input.txt', 'r') as input_handle:
    numbers = input_handle.read().split()

numbers = list(map(int, numbers))

def solve(length):
    for c in combinations(numbers, length):
        if sum(c) == 2020:
            return prod(c)

print(solve(2))
