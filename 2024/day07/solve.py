import sys

input = open(sys.argv[1]).read().strip().split('\n')

def resolve(q, index, res, val):
    if len(q) == index:
        return res == val
    e = q[index]
    return resolve(q, index + 1, res + e, val) or resolve(q, index + 1, res * e, val)

sum=0
for line in input:
    q = []
    val = int(line.split(':')[0])
    l = line.split(':')[1].strip().split(' ')
    for n in l:
        q.append(int(n))
    if resolve(q, 1, q[0], val):
        sum += val
print(sum)
    
