import sys

input = open(sys.argv[1]).read().strip().split('\n')

def resolve_advanced(q, index, res, val, op):
    if len(q) == index:
        return res == val
    e = q[index]
    if op == '+':
        res += e
    elif op == '*':
        res *= e
    elif op == "||":
        n = 1
        temp = e
        while int(temp) > 0:
            temp /= 10
            n *= 10
        res *= n
        res += e
    return resolve_advanced(q, index + 1, res, val, "||") or \
           resolve_advanced(q, index + 1, res, val, '+') or \
           resolve_advanced(q, index + 1, res, val, '*')

def resolve(q, index, res, val):
    if len(q) == index:
        return res == val
    e = q[index]
    return resolve(q, index + 1, res + e, val) or resolve(q, index + 1, res * e, val)

sum=0
for line in input:
    q = []
    val = int(line.split(':')[0])
    l = line.split(':')[1].strip().split(' ')
    for n in l:
        q.append(int(n))
    if resolve(q, 1, q[0], val) or resolve_advanced(q, 0, q[0], val, '/'):
        sum += val
print(sum)
    
