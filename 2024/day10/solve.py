import sys

input = open(sys.argv[1]).read().strip().split('\n')
leni, lenj = len(input), len(input[0])

def calculate_score(i, j, score, uniques_9):
    if input[i][j] == '9' and (i, j) not in uniques_9:
        uniques_9.add((i, j))
        return score + 1
    choices = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    for pos in choices:
        if 0 <= pos[0] < leni and 0 <= pos[1] < lenj and input[pos[0]][pos[1]] == str(int(input[i][j]) + 1):
            score = calculate_score(pos[0], pos[1], score, uniques_9)
    return score
            

sum=0   
for i, line in enumerate(input):
    for j, c in enumerate(line):
        if c == '0':
            sum += calculate_score(i, j, 0, set())
print(sum)
