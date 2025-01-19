import sys
from collections import defaultdict

input = open(sys.argv[1]).read().strip().split('\n\n')
moves = "".join(input[1].split('\n'))
left = input[0].split('\n')

board = []
for i, line in enumerate(left):
    a = []
    for j, c in enumerate(line):
        if c == '@':
            p = (i, j)
        a.append(c)
    board.append(a)

#directions
d = ['^', '<', '>', 'v']
#up or down
dx = [-1, 0, 0, 1]
#left or right
dy = [0, -1, 1, 0]

for m in moves:
    idx = d.index(m)
    stack = [p]
    x, y = p[0] + dx[idx], p[1] + dy[idx]
    while True:
        stack.append((x, y))
        if board[x][y] == '.' or board[x][y] == '#':
            break
        x, y = x + dx[idx], y + dy[idx]
    pp = stack.pop()  
    if board[pp[0]][pp[1]] == '#':
        continue
    while len(stack) > 0:
        pn = stack.pop()
        board[pp[0]][pp[1]] = board[pn[0]][pn[1]]
        board[pn[0]][pn[1]] = '.'
        p = pp
        pp = pn

res = 0
for i, line in enumerate(board):
    for j, c in enumerate(line):
        if c == 'O':
            res += 100 * i + j
print(res)

"""
for line in board:
    print("".join(line))
"""