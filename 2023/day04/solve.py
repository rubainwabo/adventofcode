import sys

input = open(sys.argv[1]).read().strip()

for line in input.split('\n'):
    data = line.split(':')[1].strip().split('|')
    pts = data[0].strip().split(' ')
    nbrs = data[1].strip().split(' ')

    print(pts)
    print(nbrs)