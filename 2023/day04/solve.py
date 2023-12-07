import sys

input = open(sys.argv[1]).read().strip()

total=0

for line in input.split('\n'):
    data = line.split(':')[1].strip().split('|')
    pts = data[0].strip().split(' ')
    nbrs = data[1].strip().split(' ')

    score=0
    for nbr in nbrs:
        for pt in pts:
            if pt.isdigit() and nbr.isdigit():
                if pt == nbr and score==0:
                    score = 1
                elif pt == nbr:
                    score*=2 
    total+=score
print(total)
            