import sys


input = open(sys.argv[1]).read().strip()

maps=[[] for i in range(7)]

arr=-1
for line in input.split('\n'):
    if line.startswith("seeds"):
        seeds=line.split(':')[1].strip().split(' ')
    elif len(line.strip())!=0 and line[0].isdigit():
        sline = line.split(' ')
        #src dest range
        #seed to soil (seed = src, soil = dest)
        maps[arr].append([int(sline[1]),int(sline[0]),int(sline[2])])
    elif len(line.strip())==0:
        arr+=1

locations=[]

def lookup(_map, val):
    for i in range(len(_map)):
        if _map[i][0]<=val<=_map[i][0]+_map[i][2]:
            diff = _map[i][0]+_map[i][2] - val
            return _map[i][2] + _map[i][1] - diff
    return val

for i in range(len(seeds)):
    r = int(seeds[i])
    for j in range(7):
        r = lookup(maps[j], r)
    locations.append(r)

locations.sort()
print(locations[0])
