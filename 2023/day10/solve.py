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
    '.': [0,0,0,0],
    'S': [1,-1,-1,1],
}

lenI = len(M)
lenJ = len(M[0])
def find_next():
    i=s[0]
    j=s[1]
    #North
    if i-1>=0 and 1+D[M[i-1][j]][1]==0:
        return tuple((i-1, j, 2))
    #South
    elif i+1<lenI and 1-D[M[i+1][j]][0]==0:
        return tuple((i+1, j, 1))
    #West
    elif j-1>=0 and 1-D[M[i][j-1]][3]==0:
        return tuple((i, j-1, 4))
    #East
    elif j+1<lenJ and 1+D[M[i][j+1]][2]==0:
        return tuple((i, j+1, 3))
    return None
s = find_next()
i=s[0]
j=s[1]
pt=M[i][j]
n=0
#N=1 S=2 W=3 E=4
visited=s[2]
while True:
    if pt=='S':
        break
    elif pt=='L':
        if i-1>=0 and 1+D[M[i-1][j]][1]==0 and visited!=1:
            s=tuple((i-1, j, 2))
        elif j+1<lenJ and 1+D[M[i][j+1]][2]==0 and visited!=4:
            s=tuple((i, j+1, 3))
    elif pt=='-':
        if j-1>=0 and 1-D[M[i][j-1]][3]==0 and visited!=3:
            s=tuple((i, j-1, 4))
        elif j+1<lenJ and 1+D[M[i][j+1]][2]==0 and visited!=4:
            s=tuple((i, j+1, 3))
    elif pt=='F':
        if i+1<lenI and 1-D[M[i+1][j]][0]==0 and visited!=2:
            s=tuple((i+1, j, 1))
        elif j+1<lenJ and 1+D[M[i][j+1]][2]==0 and visited!=4:
            s=tuple((i, j+1, 3))
    elif pt=='J':
        if i-1>=0 and 1+D[M[i-1][j]][1]==0 and visited!=1:
            s=tuple((i-1, j, 2))
        elif j-1>=0 and 1-D[M[i][j-1]][3]==0 and visited!=3:
            s=tuple((i, j-1, 4))
    elif pt=='|':
        if i-1>=0 and 1+D[M[i-1][j]][1]==0 and visited!=1:
            s=tuple((i-1, j, 2))
        elif i+1<lenI and 1-D[M[i+1][j]][0]==0 and visited!=2:
            s=tuple((i+1, j, 1))
    elif pt=='7':
        if i+1<lenI and 1-D[M[i+1][j]][0]==0 and visited!=2:
            s=tuple((i+1, j, 1))
        elif j-1>=0 and 1-D[M[i][j-1]][3]==0 and visited!=3:
            s=tuple((i, j-1, 4))
    i=s[0]
    j=s[1]
    visited=s[2]
    pt=M[i][j]
    n+=1
print(int(n/2)+1)