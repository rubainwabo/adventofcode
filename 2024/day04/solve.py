import sys

input = open(sys.argv[1]).read().strip().split('\n')

count=0
leni, lenj= len(input), len(input[0])

# (di, dj) reprensents the direction
# k reprensents the distance
# (i, j) represents the actual position
# (ni, nj) reprensents the position obtained after applying the direction and the distance
def check_direction(i, j, di, dj):
    s=""
    for k in range(1,4):
        ni, nj = i + di*k, j + dj*k
        if 0 <= ni < leni and 0 <= nj < lenj:
            s += input[ni][nj]
        else:
            break
    return s=="MAS"

for i in range(leni):
    for j in range(lenj):
        if input[i][j]=='X':
            if check_direction(i, j, 0, 1): #check right
                count+=1
            if check_direction(i, j, 0, -1): #check left
                count+=1
            if check_direction(i, j, -1, 0): #check up
                count+=1
            if check_direction(i, j, 1, 0): #check down
                count+=1
            if check_direction(i, j, -1, 1): #check down left
                count+=1
            if check_direction(i, j, 1, 1): #check down right
                count+=1
            if check_direction(i, j, 1, -1): #check up right
                count+=1
            if check_direction(i, j, -1, -1): #check up left
                count+=1
print(count)