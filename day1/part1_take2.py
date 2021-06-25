from math import prod
from itertools import combinations

with open('E:\code\AoC\day1\input.txt', 'r') as input_handle:
    numbers = input_handle.read().split()

numbers = list(map(int, numbers))

def solve(length):
    for c in combinations(n, length):
        if sum(c) == 2020:
            return prod(c)


n = [line for line in numbers]
print(solve(2))