import sys

input = open(sys.argv[1]).read().strip()
l = len(input)

def checkSum(s):
    left = 0
    right = len(s) - 1
    sum = 0
    while left < right:
        if s[left] == None and s[right] != None:
            s[left] = s[right]
            s[right] = None
            right -= 1
            left += 1
        elif s[right] == None:
            right -= 1
        elif s[left] != None:
            left += 1
    left = 0
    while s[left] != None:
        sum += left * s[left]
        left += 1
    return sum

def initial_representation():
    index=0
    blocks = []
    for i in range(l):
        v = int(input[i])
        if i % 2 == 0:
            for _ in range(v):
                blocks.append(index)
            index += 1
        else:
            for _ in range(v):
                blocks.append(None)
    return blocks

print(checkSum(initial_representation()))