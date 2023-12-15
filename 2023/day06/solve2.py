import sys
import time
from functools import reduce


start = time.time()
t,d = open(sys.argv[1]).read().strip().split('\n')
t = t.split(':')[1].strip().split(' ')
d = d.split(':')[1].strip().split(' ')

T = int(reduce(lambda a,b: a+b, t))
D = int(reduce(lambda a,b: a+b, d))

n=0
for x in range(1, T):
    if x*(T-x)>D:
        n+=1
end = time.time()
print(f'result: {n} in {end-start} seconds')