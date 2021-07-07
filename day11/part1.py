with open('E:\code\AoC\day11\input.txt', 'r') as fp:
    #help(type(fp).readlines)
    lines = [line.rstrip() for line in fp.readlines()]
    lines = [list(line) for line in lines]
    #print(lines)

#print('there are', len(lines), 'rows')
#print('there are', len(lines[0]), 'columnes')
rows, cols = len(lines), len(lines[0])
deltas = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

"""We are identifying the positions around the seats, 
 the eight positions around the seats are like this:

      111
      101
   => 111

the arrow marks the position for row and column that would be
-1 and -1 in relation to 0, so the position relative to 0 is (-1,-1)
we omit the 0 position in deltas"""

#Counts the amount of occupied sits around the given position in the grid
#this is important to check if there are atleast 4 seats occupied so we can know if they will leave
def count_occupied(r, c, grid):
    count=0
    for i,j in deltas:
        xi,xj=r+i,c+j
        if 0<=xi<rows and 0<=xj<cols and grid[xi][xj]=='#':
            count+=1
    return count

#help(list.copy)
def check_occupied(lines, thresh = 4):
    while True:
        valid = True
        temp_grid=[r.copy() for r in lines]
        for i, r in enumerate(temp_grid):     #looping through the row-index and rows in the grid
            for j, c in enumerate(r):         #looping through the columns-index and columns in the grid
                count = count_occupied(i, j, temp_grid)
                if c=='L' and count==0:
                    lines[i][j]='#'
                elif c=='#' and count>=thresh:
                    lines[i][j]='L'
                valid&=(r[j]==lines[i][j])
        if valid:
            break

    ans=0
    for i in range(rows):
        for j in range(cols):
            if lines[i][j]=='#':
                ans+=1
    print(f"There are {ans} valid seats.")
check_occupied(lines)