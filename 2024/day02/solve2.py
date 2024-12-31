import sys

input = open(sys.argv[1]).read().split('\n')

def is_safe(nums):
    for i in range(0, len(nums)-1):
        if nums[i] - nums[i+1] not in [1,2,3]:
            return False
    return True

def fixed_unsafe(nums):
    if is_safe(nums):
        return True
    for i in range(0, len(nums)):
        if is_safe(nums[:i]+nums[i+1:]):
            return True
    return False

sum=0
for line in input:
    line = [int(x) for x in line.split(' ')]
    if line[len(line)-1] > line[0]:
        line.reverse()
    sum += fixed_unsafe(line)
print(sum)