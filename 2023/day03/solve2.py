import sys

input = open(sys.argv[1]).read().strip()

t = [[i for i in line] for line in input.split('\n')]
for i in range(len(t)):
    t[i].append('.')
lenI = len(t)
lenJ = len(t[0])
result=0
for i in range(len(t)):
    for j in range(len(t[i])):
        if t[i][j]=='*':
            myset=set()
            for ii in [-1,0,1]:
                for jj in [-1,0,1]:
                    if 0<=i+ii<lenI and 0<=j+jj<lenJ:
                        car = t[i+ii][j+jj]
                        if car.isdigit():
                            index = j+jj - 1
                            sleft=''
                            sright=''
                            while index>=0 and t[i+ii][index].isdigit():
                                sleft = t[i+ii][index] + sleft
                                index-=1
                            index = j+jj + 1
                            while index<lenJ and t[i+ii][index].isdigit():
                                sright += t[i+ii][index]
                                index+=1
                            myset.add(int(sleft + car + sright))
                            print(myset)
            if len(myset)==2:
                mul=1
                for n in myset:
                    mul *= n
                result+=mul
print(result)