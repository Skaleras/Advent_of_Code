from math import ceil as round_up
data = open('E:\code\AoC\day5\input.txt', 'r')
my_input = data.read()
seats = my_input.split('\n')

seat_ids = list()
for seat in seats:

    seat_row, seat_column = seat[:7], seat[7:]  # Separating the problem in row position and column position
    n = 1
    row_range = [0, 127]
    column_range = [0, 7]
    while n != 8:     # row position, the first 7 letters
        if seat_row[n-1]=='F':     #lower half
            row_range[1] = (sum(row_range))//2
            n+=1
            if n==8:
                row = row_range[1]
        else:                       #upper half
            row_range[0] = round_up((sum(row_range))/2)
            n+=1
            if n==8:
                row = row_range[0]
                
    n = 1
    while n != 4:     # column position, the last 3 letters
        if seat_column[n-1]=='L':    #lower half
            column_range[1] = (sum(column_range))//2
            n+=1
            if n==4:
                column = column_range[0]
        else:                        #upper half
            column_range[0] = round_up((sum(column_range))/2)
            n+=1
            if n==4:
                column = column_range[1]
                
    seat_id = row*8 + column
    seat_ids.append(seat_id)

print(max(seat_ids))
