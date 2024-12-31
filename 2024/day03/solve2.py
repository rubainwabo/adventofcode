import sys
import re

input = open(sys.argv[1]).read().strip()

ins=0

pattern = r"mul\(-?\d+,-?\d+\)"
matches = re.findall(pattern, input)
j=0
ans=0
for i in range(len(input)):
    if "do()"==input[i:i+4]:
        ins=1
    if "don't()"==input[i:i+7]:
        ins=-1
    if j < len(matches) and i + len(matches[j]) < len(input)+1 and matches[j]==input[i:i+len(matches[j])]:
        if ins==0 or ins==1:
            pattern = r"(-?\d+)"
            m = re.findall(pattern, matches[j])
            ans+=int(m[0])*int(m[1])
        j+=1
print(ans)
