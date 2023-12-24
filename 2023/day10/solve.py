import sys

input = open(sys.argv[1]).read().strip().split('\n')

M=[]
s=tuple()
for i in range(len(input)):
    T=[]
    for j in range(len(input[i])):
        if input[i][j]=='S':
            s = tuple((i, j))
        T.append(input[i][j])
    M.append(T)

#NSWE
D = {
    'L':[1,0,0,1],
    'F': [0,-1,0,1],
    '7': [0,-1,-1,0],
    '-': [0,0,-1,1],
    '|': [1,-1,0,0],
    'J': [1,0,-1,0],
    '.': [0,0,0,0]
}

lenI = len(M)
lenJ = len(M[0])
def find_next():
    i=s[0]
    j=s[1]
    #North
    if i-1>=0 and 1-D[M[i-1][j]][0]==0:
        return tuple((i-1, j))
    #South
    elif i+1<lenI and 1+D[M[i+1][j]][1]==0:
        return tuple((i+1, j))
    #West
    elif j-1>=0 and 1+D[M[i][j-1]][2]==0:
        return tuple((i, 1))
    #East
    elif j+1<lenJ and 1-D[M[i][j+1]][3]==0:
        return tuple((i, j+1))
    return None
s = find_next()
n=0
while True:
    if s=='S':
        break
