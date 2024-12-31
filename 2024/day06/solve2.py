import sys


input = open(sys.argv[1]).read().strip().split('\n')
# The guard goes forward until it hits an obstacle then turns right,... The process is repeated until the guard leaves the grid.

board = [list(line) for line in input]
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

def find_positions_for_O():
    cur_dir = 0
    positions = set()
    leni, lenj= len(board), len(board[0])
    i, j = pos_guard()
    while 0 <= i < leni and 0 <= j < lenj:
        ni, nj = i + di[cur_dir], j + dj[cur_dir]

        if 0 <= ni < leni and 0 <= nj < lenj and board[ni][nj] != '#':
            positions.add((i, j))
            i, j = ni, nj
        elif 0 <= ni < leni and 0 <= nj < lenj and board[ni][nj] == '#':
            cur_dir = (cur_dir + 1) % 4
        else:
            positions.add((i, j))
            break
    return positions

def resolve():
    visited = set()
    cur_dir = 0
    leni, lenj= len(board), len(board[0])
    i, j = pos_guard()
    while 0 <= i < leni and 0 <= j < lenj:
        state = (i, j, cur_dir)
        if state in visited:
            return True
        visited.add(state)

        ni, nj = i + di[cur_dir], j + dj[cur_dir]

        if 0 <= ni < leni and 0 <= nj < lenj and board[ni][nj] != '#' and board[ni][nj] != 'O':
            i, j = ni, nj
        elif 0 <= ni < leni and 0 <= nj < lenj and (board[ni][nj] == '#' or board[ni][nj] == 'O'):
            cur_dir = (cur_dir + 1) % 4
        else:
            break
    return False

   
positions = find_positions_for_O()
positions.remove(pos_guard())
count = 0

for p in positions:
    board[p[0]][p[1]] = 'O'
    if resolve():
        count += 1
    board[p[0]][p[1]] = '.'


print(count)