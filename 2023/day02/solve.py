import sys
import re

input = open(sys.argv[1]).read().strip()
total = 0

BLUE = 14
GREEN = 13
RED = 12
pattern = r',|;'

for line in input.split('\n'):
    flag = True
    arr = line.split(':')
    game = int(arr[0].split()[1])
    t = re.split(pattern, arr[1])
    for val in t:
        l = val.split()
        if ((l[1]=='green' and int(l[0])>GREEN) or (l[1]=='blue' and int(l[0])>BLUE) or (l[1]=='red' and int(l[0])>RED)):
            flag = False
            break
    if flag:
        total += game
print(total)