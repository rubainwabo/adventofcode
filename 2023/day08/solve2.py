import math
import sys
import time

start = time.time()

ins, rest = open(sys.argv[1]).read().strip().split('\n\n')

D = {}
st = []
for o in rest.split('\n'):
    s, n = o.split('=')
    l, r = n.strip().split(',')
    s = s.strip()
    l = l.split('(')[1]
    r = r.split(')')[0].strip()

    if s.endswith('A'):
        st.append(s)

    D[s]=[l, r]


def depth(p):
    idx=0
    while not p.endswith('Z'):
        if ins[idx%len(ins)]=='L':
            p = D[p][0]
        else:
            p = D[p][1]
        idx+=1
    return idx

P = [depth(x) for x in st]
print(*P)
res = math.lcm(*P)
end=time.time()
print(f'{res} in {end-start}')