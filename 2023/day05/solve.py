import sys


input = open(sys.argv[1]).read().strip()

maps=[[] for i in range(7)]

a=-1
for line in input.split('\n'):
    if line.startswith("seeds"):
        seeds=line.split(':')[1].strip().split(' ')
    elif len(line.strip())!=0 and line[0].isdigit():
        x, y, z = line.split(' ')
        #src dest range
        #seed to soil (seed = src, soil = dest)
        maps[a].append([int(y),int(x),int(z)])
    elif len(line.strip())==0:
        a+=1

locations=[]

def lookup(_map, val):
    for i in range(len(_map)):
        if _map[i][0]<=val<=_map[i][0]+_map[i][2]:
            return _map[i][1] + val - _map[i][0]
    return val

for i in range(len(seeds)):
    r = int(seeds[i])
    for j in range(7):
        r = lookup(maps[j], r)
    locations.append(r)

locations.sort()
print(locations[0])
