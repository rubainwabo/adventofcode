import sys
import re

input = open(sys.argv[1]).read().strip()

pattern = r"mul\((-?\d+),(-?\d+)\)"
matches = re.findall(pattern, input)
ans = 0
for num1, num2 in matches:
    ans += int(num1) * int(num2)
print(ans)