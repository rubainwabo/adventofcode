import sys


input = open(sys.argv[1]).read().strip()

maps=[[] for i in range(7)]

dic = {}

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

for i in range(0,len(seeds),2):
    if i+1<len(seeds):
        for j in range(int(seeds[i+1])-1, -1, -1):
            if dic.get(str(int(seeds[i])+j))!=None:
                continue
            else:
                seed = int(seeds[i]) + j
                soil = lookup(maps[0], seed)
                fert = lookup(maps[1], soil)
                water = lookup(maps[2], fert)
                light = lookup(maps[3], water)
                temp = lookup(maps[4], light)
                hum = lookup(maps[5], temp)
                loc = lookup(maps[6], hum)
                locations.append(loc)
                dic[str(int(seeds[i])+j)]=loc


locations.sort()
print(locations[0])
