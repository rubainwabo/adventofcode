import sys

input = open(sys.argv[1]).read().strip()
l = len(input)

def checkSum(b, weigths):
    right = len(weigths) - 1
    while right > 0:
        left = 1
        while left < right:
            free_space = weigths[left]
            files = weigths[right]
            if files[1] - files[0] <= free_space[1] - free_space[0]:
                for i in range(files[0], files[1]):
                    b[free_space[0] + (i - files[0])] = b[files[0]]
                for i in range(files[0], files[1]):
                    b[i] = None
                weigths[left] = (free_space[0] + (files[1] - files[0]), free_space[1])
                break
            left += 2
        right-=2
    size = len(b)
    sum=0
    for i in range(size):
        if b[i] != None:
            sum += i * b[i]
    return sum

def initial_representation():
    index_file = 0
    blocks = []
    st = 0
    ed = 0
    weigths = []
    for i in range(l):
        v = int(input[i])
        if i % 2 == 0:
            for _ in range(v):
                blocks.append(index_file)
                ed += 1
            index_file += 1
            weigths.append((st, ed))
        else:
            for _ in range(v):
                blocks.append(None)
                ed += 1
            if v > 0 :
                weigths.append((st, ed))
            else :
                weigths.append((-1, -1))
        st = ed
    return blocks, weigths

blocks, weigths = initial_representation()
print(checkSum(blocks, weigths))