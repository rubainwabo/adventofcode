import sys
import math
from collections import defaultdict

input = open(sys.argv[1]).read().strip().split(' ')
stones = [int(n) for n in input]

nums = defaultdict(int)
for n in stones:
    nums[n] += 1

def blink_stones(nums: dict):
    new_nums = defaultdict(int)
    for n in nums:
        if n > 0:
            digits = math.floor(math.log10(n)) + 1
        if n == 0:
            new_nums[1] += nums[n]
        elif digits % 2 == 0:
            factor = 10 ** (digits // 2)
            new_nums[n // factor] += nums[n]
            new_nums[n % factor] += nums[n]
        else:
            new_nums[n * 2024] += nums[n]
    return new_nums

for _ in range(75):
    nums = blink_stones(nums)

res = 0
for n in nums:
    res += nums[n]
print(res)