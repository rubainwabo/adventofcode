import sys
from collections import defaultdict

input = open(sys.argv[1]).read().strip().split('\n')
board = [list(line) for line in input]
leni, lenj = len(input), len(input[0])

def find_region(regions, car, pos, car_saved, visited):
    if input[pos[0]][pos[1]] != car:
        return
    visited.add(pos)
    regions[car_saved].add(pos)
    i, j = pos[0], pos[1]
    board[i][j] = car_saved
    choices = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    for ch in choices:
        if 0 <= ch[0] < leni and 0 <= ch[1] < lenj and input[ch[0]][ch[1]] == car and ch not in visited:
            find_region(regions, car, ch, car_saved, visited)

def determine_regions():
    r = defaultdict(set)
    visited = set()
    for i, line in enumerate(input):
        for j, c in enumerate(line):
            car, car_saved = input[i][j], input[i][j]
            if (i, j) not in visited:
                while car_saved in r:
                    car_saved += car
                find_region(r, car, (i,j), car_saved, visited)
    return r

def calculate_perimeters():
    p = defaultdict(int)
    for i, line in enumerate(board):
        for j, c in enumerate(line):
            choices = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for ch in choices:
                if 0 <= ch[0] < leni and 0 <= ch[1] < lenj and board[ch[0]][ch[1]] == c:
                    continue
                else:
                    p[c] += 1
    return p

regions = determine_regions()
perimeters = calculate_perimeters()

"""
print("Board after finding the regions : ")
for x in range(leni):
    for y in range(lenj):
        print(board[x][y], end=" ")
    print()
"""

res = 0
for r in regions:
    res += len(regions[r]) * perimeters[r]
print(res)