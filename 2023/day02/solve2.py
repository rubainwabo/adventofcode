import sys

input = open(sys.argv[1]).read().strip()

total = 0

for line in input.split('\n'):
    #red, green, blue
    max = [1,1,1]
    t = line.split(':')[1].split(';')
    for e in t:
        l = e.split(',')
        for i in l:
            k = i.split()
            if k[1] == 'red':
                if int(k[0]) > max[0]:
                    max[0] = int(k[0])
            elif k[1] == 'green':
                if int(k[0]) > max[1]:
                    max[1] = int(k[0])
            elif k[1] == 'blue':
                if int(k[0]) > max[2]:
                    max[2] = int(k[0])
    total += max[0]*max[1]*max[2]
print(total)