import sys
import re

input = open(sys.argv[1]).read().strip().split('\n')
# A (X, Y) B (X, Y) Prize (X, Y)
nums = []

def isValid(nbr):
    if nbr < 0:
        return False
    s = str(nbr)
    right = s.split('.')[1]
    if right != '0':
        return False
    return True

def solve_equations(A, B, P):
    P = (P[0] + 10000000000000, P[1] + 10000000000000)
    _b_x = -1 * B[0] * A[1]
    _b_y = A[0] * B[1]
    _p_x = -1 * A[1] * P[0]
    _p_y = A[0] * P[1]

    y = (_p_y + _p_x) / (_b_y + _b_x)
    x = (P[0] - (y * B[0])) / A[0]
    if not isValid(x) or not isValid(y):
        return (-1, -1)
    return (int(x), int(y))    

for line in input: 
    n = re.findall(r'\b\d+\b', line)
    if n != []:
        nums.append((int(n[0]), int(n[1])))

res = 0
for i in range(len(nums)):
    if i%3 == 0:
        x, y = solve_equations(nums[i], nums[i + 1], nums[i + 2])
        if x != -1 and y != -1:
            res += x * 3 + y
print(res)
