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

def antinodes(a1, a2):
    dx = a2[0] - a1[0]
    dy = a2[1] - a1[1]
    d = (dx, dy)
    return sub_tuples(a1, d), sum_tuples(a2, d)

def resolve(antennas, uniques):
    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            ant1, ant2 = antinodes(antennas[i], antennas[j])
            ant1_in_bounds = is_within_bounds(ant1, leni, lenj)
            ant2_in_bounds = is_within_bounds(ant2, leni, lenj)
            if ant1_in_bounds:
                uniques.add(ant1)
            if ant2_in_bounds:
                uniques.add(ant2)
 
            
for i, line in enumerate(input):
    for j, c in enumerate(line):
        if 'A' <= c <= 'Z' or 'a' <= c <= 'z' or '0' <= c <= '9':
            d.setdefault(c, []).append((i, j))

uniques=set()
for k,v in d.items():
    resolve(v, uniques)

print(len(uniques))    
