import sys

input = open(sys.argv[1]).read().strip().split('\n')
leni, lenj = len(input), len(input[0])

def calculate_score(i, j, score):
    if input[i][j] == '9' and (i, j):
        return score + 1
    choices = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    for pos in choices:
        if 0 <= pos[0] < leni and 0 <= pos[1] < lenj and input[pos[0]][pos[1]] == str(int(input[i][j]) + 1):
            score = calculate_score(pos[0], pos[1], score)
    return score
            

sum=0   
for i, line in enumerate(input):
    for j, c in enumerate(line):
        if c == '0':
            sum += calculate_score(i, j, 0)
print(sum)
