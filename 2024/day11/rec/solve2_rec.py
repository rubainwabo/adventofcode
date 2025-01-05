import sys
import math

input = open(sys.argv[1]).read().strip().split(' ')

blink_cache = {}
count_cache = {}

def blink_a_stone(stone):
    if stone in blink_cache:
        return blink_cache[stone]
    
    if stone > 0:
        digits = math.floor(math.log(stone, 10)) + 1

    if stone == 0:
        result = (1, None)
    elif digits % 2 == 0:
        mid = digits // 2
        x = 10 ** mid
        result = (stone // x, stone % x)
    else:
        result = (stone * 2024, None)
    
    blink_cache[stone] = result
    return result

def count_blinks(stone, depth):
    if (stone, depth) in count_cache:
        return count_cache[(stone, depth)]

    left, right = blink_a_stone(stone)
    if depth == 1:
        if right is None:
            result = 1
        else:
            result = 2
    else:
        result = count_blinks(left, depth - 1)
        if right is not None:
            result += count_blinks(right, depth - 1)
    
    count_cache[(stone, depth)] = result
    return result

def solve(counter):
    total = 0

    for stone in input:
        total += count_blinks(int(stone), counter)
    return total

print(solve(75))
