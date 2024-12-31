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
for i in range(0, len(left_numbers)):
    sum+=max(left_numbers[i], right_numbers[i])-min(left_numbers[i], right_numbers[i])

print(sum)