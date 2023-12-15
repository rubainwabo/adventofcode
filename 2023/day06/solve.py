import sys


t,d = open(sys.argv[1]).read().strip().split('\n')
t = t.split(':')[1].strip().split(' ')
d = d.split(':')[1].strip().split(' ')

T = []
D = []

for i in range(len(t)):
    if t[i].isdigit():
        T.append(int(t[i]))
for i in range(len(d)):
    if d[i].isdigit():
        D.append(int(d[i]))

m=1
for i in range(len(T)):
    x = T[i]
    n=0
    for xx in range(1, x):
        if xx*(x-xx)>D[i]:
            n+=1
    m*=n
print(m)

    


