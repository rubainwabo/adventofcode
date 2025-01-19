import sys
from collections import defaultdict
from functools import reduce

input = open(sys.argv[1]).read().strip().split('\n\n')
moves = "".join(input[1].split('\n'))
left = input[0].split('\n')

board = []
for i, line in enumerate(left):
    a = []
    for j, c in enumerate(line):
        if c == '#':
            a.append("#")
            a.append("#")
        elif c == 'O':
            a.append("[")
            a.append("]")
        elif c == '.':
            a.append(".")
            a.append(".")
        elif c == '@':
            p = (i, j * 2)
            a.append("@")
            a.append(".")
    board.append(a)

#print(p)

#directions
d = ['^', '<', '>', 'v']
#up or down
dx = [-1, 0, 0, 1]
#left or right
dy = [0, -1, 1, 0]
counter = [0, 0, 0, 0]

def print_board():
    _board = []
    for line in board:
        a = []
        for e in line:
            a.append(e)
        _board.append(a)
    for line in _board:
        print("".join(line))


#idx = 0 or idx = 3
def vertical_stacking(stack, idx):
    st = [stack[-1]]
    while len(st) > 0:
        last = st.pop()
        for l in last:
            if board[l[0]][l[1]] == '#':
                print("Can't Push :(")
                print(f"before returning what we found with last {last} ", end="")
                for l in last:
                    print(f"{board[l[0]][l[1]]}", end="")
                print()
                return False
        if len(last) == reduce(lambda count, c: count + (1 if board[c[0]][c[1]] == '.' else 0), last, 0):
            print("Can Push :)")
            print(f"before returning what we found with last {last} ", end="")
            for l in last:
                print(f"{board[l[0]][l[1]]}", end="")
            print()            
            return True
        a = set()
        for l in last:
            if board[l[0]][l[1]] == '.':
                continue
            x, y = l[0] + dx[idx], l[1] + dy[idx]
            a.add((x, y))
            if board[x][y] == '[':
                a.add((x, y + 1))
            elif board[x][y] == ']':
                a.add((x, y - 1))
        st.append(a)
        stack.append(a)
        print("Elements in the stack : ", end="")
        for i, elts in enumerate(stack):
            print(f"pos {i+1} ", end="")
            for l in elts:
                print(f"{board[l[0]][l[1]]} ", end="")
        print()                 
        #print(f"stack in vertical stacking {stack}")

def vertical_unstacking(stack, idx):
    stack.pop()
    #print(f"inside vertical unstacking : {stack}")
    while len(stack) > 0:
        elts = stack.pop()
        for e in elts:
            if board[e[0]][e[1]] == '.':
                continue
            x, y = e[0] + dx[idx], e[1] + dy[idx]            
            board[x][y] = board[e[0]][e[1]]
            board[e[0]][e[1]] = '.'
            p = (x, y)
    return p   



for m in moves:
    idx = d.index(m)
    counter[idx] += 1
    if idx==3 and counter[idx]==1081:
            print_board()
    if idx == 1 or idx == 2:
        #print(f"{counter[idx]} horizontal {m}")
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
    else:
        stack = [[p]]
        ##print(stack)
        print(f"{counter[idx]} vertical move {m} idx = {idx} stack {stack}")
        if vertical_stacking(stack, idx):
            p = vertical_unstacking(stack, idx)
            #print(f"p from vertical unstacking {p}")
        if idx==3 and counter[idx]==1081:
            print_board()
#print(p)

res = 0
for i, line in enumerate(board):
    for j, c in enumerate(line):
        if c == '[':
            res += 100 * i + j
print(res)


