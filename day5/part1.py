data = open('E:\code\AoC\day5\input.txt', 'r')
my_input = data.read()
seats = my_input.split('\n')
row_range = (0, 127)
column_range = (0, 7)
seat_ids = list()
for seat in seats:
    n = 1
    seat_row, seat_column = seat[:7], seat[7:]  # Separating the problem in row position and column position
    
    while n != 8:     # row position, the first 7 letters
        if seat_row[n-1]=='F':     #lower half
            row_range = pass
            n+=1
            if n==8:
                row = row_range[0]
        elif seat_row[n-1]=='B':   #upper half
            row_range = pass
            n+=1
            if n==8:
                row = row_range[1]
                
    n = 1
    while n != 4:     # column position, the last 3 letters
        if seat_column[n-1]=='L':    #lower half
            column_range = pass
            n+=1
            if n==4:
                column = column_range[0]
        elif seat_column[n-1]=='R':   #upper half
            column_range = pass
            n+=1
            if n==4:
                column = column_range[1]
                
    seat_id = row*8 + column
    seat_ids.append(seat_id)
    row_range = (0, 127)
    column_range (0, 7)
print(max(seat_ids))

# WIP
# I could have used else instead of elif since there are only two possibles events in this case
# I'm having trouble thinking about a proper way to select the ranges for the rows and columns
# to update the variable.