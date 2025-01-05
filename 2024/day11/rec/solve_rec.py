import sys

input = open(sys.argv[1]).read().strip().split(' ')

def blink_a_stone(val):
    t = str(val)
    digits = len(t)

    if val == 0:
        return (1, None)
    elif digits % 2 == 0:
        mid = digits // 2
        return (int(t[ : mid]), int(t[mid : ]))
    else :
        return (val * 2024, None)

def count_blinks(stone, depth):
    left, right = blink_a_stone(stone)

    if depth == 1:
        if right == None:
            return 1
        else:
            return 2
    else:
        out = count_blinks(left, depth - 1)
        if right is not None:
            out += count_blinks(right, depth - 1)
    return out

def solve(counter):
    out = 0

    for stone in input:
        out += count_blinks(int(stone), counter)
    return out

print(solve(25))

