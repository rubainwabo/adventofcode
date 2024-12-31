import sys
import time

input = open(sys.argv[1]).read().strip().split('\n')
# The guard goes forward until it hits an obstacle then turns right,... The process is repeated until the guard leaves the grid.

board = [list(line) for line in input]
dirs = ['^', '>', 'v', '<']
#Up, Right, Down, Left
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def pos_guard():
    i, j = 0, 0
    for x, line in enumerate(board):
        if '^' in line:
            i, j = x, line.index('^')
            break
    return (i, j)

def resolve():
    cur_dir = 0
    positions = set()
    leni, lenj= len(board), len(board[0])
    i, j = pos_guard()
    while 0 <= i < leni and 0 <= j < lenj:
        ni, nj = i + di[cur_dir], j + dj[cur_dir]

        if 0 <= ni < leni and 0 <= nj < lenj and board[ni][nj] != '#':
            positions.add((i, j))
            board[i][j] = '.'
            i, j = ni, nj
            board[i][j] = dirs[cur_dir]
        elif 0 <= ni < leni and 0 <= nj < lenj and board[ni][nj] == '#':
            cur_dir = (cur_dir + 1) % 4
            board[i][j] = dirs[cur_dir]
        else:
            positions.add((i, j))
            break
        # visualisation for small input
        for line in board:
            print("".join(line))
        print()
        time.sleep(1) 
        
    return positions
   
print(len(resolve()))
