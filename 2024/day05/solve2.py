import sys
from functools import cmp_to_key

input = sys.argv[1]
data = open(input).read().strip().split('\n\n')
panel_lines = data[0].split('\n')
sequence_lines = data[1].split('\n')

connections = {}
for line in panel_lines:
    k, v = line.split('|')
    connections.setdefault(k, set()).add(v)


def is_line_valid(elts):
    l = len(elts)
    middle_value = int(elts[l // 2])

    for i, elt in enumerate(elts):
        if elt in connections:
            for j in range(i + 1, l):
                if elts[j] not in connections[elt]:
                    return 0
        elif i < l - 1:
            return 0
    return middle_value

def compare(a, b):
    if a in connections:
        if b in connections[a]:
            return -1
        else:
            return 1
    else:
        if b in connections:
            if a in connections[b]:
                return 1
            else:
                return -1

sum = 0
for line in sequence_lines:
    elts = line.split(',')
    if is_line_valid(elts)==0:
        sorted_elts = sorted(elts, key=cmp_to_key(compare))
        middle_value = int(sorted_elts[len(sorted_elts) // 2])
        sum+=middle_value

print(sum)