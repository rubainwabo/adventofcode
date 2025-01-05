import sys

input = open(sys.argv[1]).read().strip().split(' ')

def convert_stones(l):
    ret = []
    for n in l:
        if n == '0':
            ret.append('1')
        elif len(n) % 2 == 0:
            mid = len(n) // 2
            ret.append(n[0 : mid])
            ni = int(n[mid : ])
            ret.append(str(ni))
        else:
            ret.append(str(int(n) * 2024))
    return ret

for _ in range(25):
    input = convert_stones(input)
print(len(input))