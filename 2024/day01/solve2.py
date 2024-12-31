import sys
import re

input = open(sys.argv[1]).read().split('\n')

left_numbers = []
right_numbers = []

for line in input:
    split = re.split(r'[ \t]+', line)
    left_numbers.append(int(split[0]))
    right_numbers.append(int(split[1]))

left_numbers.sort()
right_numbers.sort()

sum=0
for x in left_numbers:
    count = 0
    for y in right_numbers:
        if x<y:
            break
        elif x==y:
            count+=1
    sum+=(x*count)
print(sum)
