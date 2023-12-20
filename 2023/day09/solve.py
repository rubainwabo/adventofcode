from functools import reduce
import sys

input = open(sys.argv[1]).read().strip().split('\n')

def find_incr(a):
    isZero=True
    l=a[-1]
    while isZero:
        temp=[]
        i=0
        while i+1<len(a):
            temp.append(a[i+1]-a[i])
            i+=1
        a = temp
        l=l+a[-1]
        i=0
        while i<len(a):
            if a[i]!=0:
                break
            i+=1
        if i==len(a):
            isZero=False
    return l

m=0
for line in input:
    m+=find_incr([int(x) for x in line.split(' ')])
print(m)

    