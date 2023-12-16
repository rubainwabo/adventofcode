import sys

ins, rest = open(sys.argv[1]).read().strip().split('\n\n')

D = {}
for o in rest.split('\n'):
    s, n = o.split('=')
    l, r = n.strip().split(',')
    s = s.strip()
    l = l.split('(')[1]
    r = r.split(')')[0].strip()


    D[s]=[l, r]

n=0
idx=0
f='AAA'
while f!='ZZZ':
    if ins[idx%len(ins)]=='L':
        f = D[f][0]
    else:
        f = D[f][1]
    idx+=1
    n+=1
print(n)