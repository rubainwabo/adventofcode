import sys

input = open(sys.argv[1]).read().strip().split('\n')

count=0
leni, lenj= len(input), len(input[0])

# (i,j) represents the position where we found A
def check_position(i, j):
    if not (0 <= i - 1 and 0 <= j - 1 and i + 1 < leni and j + 1 < lenj):
        return False

    top_left = input[i - 1][j - 1]
    top_right = input[i - 1][j + 1]
    bottom_left = input[i + 1][j - 1]
    bottom_right = input[i + 1][j + 1]

    condition1 = top_left == top_right == 'S' and bottom_left == bottom_right == 'M'
    condition2 = top_left == top_right == 'M' and bottom_left == bottom_right == 'S'
    condition3 = top_right == bottom_right == 'S' and top_left == bottom_left == 'M'
    condition4 = top_right == bottom_right == 'M' and top_left == bottom_left == 'S'

    return condition1 or condition2 or condition3 or condition4

for i in range(leni):
    for j in range(lenj):
        if input[i][j]=='A' and check_position(i, j):
            count+=1
print(count)