import sys

input = open(sys.argv[1]).read().strip()

t = [[i for i in line] for line in input.split('\n')]
for i in range(len(t)):
    t[i].append('.')
lenI = len(t)
lenJ = len(t[0])
result=0
for i in range(len(t)):
    nbr = 0
    isPart = False
    for j in range(len(t[i])):
        if t[i][j].isdigit():
            nbr = nbr*10 + int(t[i][j])
            for ii in [-1,0,1]:
                for jj in [-1,0,1]:
                    if 0<=i+ii<lenI and 0<=j+jj<lenJ:
                        car = t[i+ii][j+jj]
                        if car.isdigit()!=True and car!='.':
                            isPart=True
        elif nbr>0:
            if isPart:
                result += nbr
            isPart=False
            nbr=0
print(result)