r = open('E:\code\AoC\day5\input.txt', 'r').read().strip('\n')
input = r.splitlines()

#Part 1
seats = [int(x.replace('F','0').replace('B','1').replace('L','0').replace('R','1'),2) for x in input]

# Inside the int function there is a conversion to binary for each seat in the input of seats in the plane
# and appends it to a list called seats using a list comprehension.
# There are only seats that are either front or back and left or right so
# it changes the base to consider the input numbers to 0's and 1's
# after that we sort it ascendingly and get the last one.

seats.sort()
print(seats[-1])