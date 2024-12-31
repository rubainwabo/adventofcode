import sys

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

sum = 0
for line in sequence_lines:
    elts = line.split(',')
    sum += is_line_valid(elts)

print(sum)