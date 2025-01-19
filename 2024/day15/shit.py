    print(f'p = {p}')
    stop = False
    last = stack[-1]
    #print(f"last = {last} and reduce = {reduce(lambda count, c: count + (1 if board[c[0]][c[1]] == '.' else 0), last, 0)}")
    for e in last:
        if e == '#':
            return False
    if len(last) == reduce(lambda count, c: count + (1 if board[c[0]][c[1]] == '.' else 0), last, 0):
        print(f"last = {last}")
        return True

    x, y = p[0] + dx[idx], p[1] + dy[idx]
    s = [(x,y)]
    if board[x][y] == '[':
        s.append((x, y + 1))
    elif board[x][y] == ']':
        s.append((x, y - 1))
    stack.append(s)
    print(f"s = {s}")
    for e in s:
        print("in my s", e)
        stop = stop or vertical_stacking(e, stack, idx)
