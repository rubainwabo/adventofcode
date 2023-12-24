import sys

input = open(sys.argv[1]).read().strip().split('\n')

def find_decr(a):
    i=0
    while i<len(a):
        if a[i]!=0:
            break
        i+=1
    if i==len(a):
        return 0 
    temp=[]
    i=0
    while i+1<len(a):
        temp.append(a[i+1]-a[i])
        i+=1
    return temp[0] - find_decr(temp)


s=0
for line in input:
    D = [int(x) for x in line.split(' ')]
    s += D[0] - find_decr(D)
print(s)

    