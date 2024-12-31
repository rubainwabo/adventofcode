import sys

input = open(sys.argv[1]).read().strip().split('\n')
d = {}
leni, lenj = len(input), len(input[0])

def sum_tuples(a, b):
    return (a[0] + b[0], a[1] + b[1])

def sub_tuples(a, b):
    return (a[0] - b[0], a[1] - b[1])

def is_within_bounds(position, rows, cols):
    return 0 <= position[0] < rows and 0 <= position[1] < cols

def antinodes(a1, a2, uniques):
    dx = a2[0] - a1[0]
    dy = a2[1] - a1[1]
    while is_within_bounds(a2, leni, lenj):
        uniques.add(a2)
        a2 = sum_tuples(a2, (dx, dy))
    while is_within_bounds(a1, leni, lenj):
        uniques.add(a1)
        a1 = sub_tuples(a1, (dx, dy))

def resolve(antennas, uniques):
    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            antinodes(antennas[i], antennas[j], uniques)
 
            
for i, line in enumerate(input):
    for j, c in enumerate(line):
        if 'A' <= c <= 'Z' or 'a' <= c <= 'z' or '0' <= c <= '9':
            d.setdefault(c, []).append((i, j))

uniques=set()
for k,v in d.items():
    resolve(v, uniques)

print(len(uniques))    
