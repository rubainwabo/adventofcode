import sys


input = open(sys.argv[1]).read().strip()

maps=[[] for i in range(7)]

dic = {}

a=-1
for line in input.split('\n'):
    if line.startswith("seeds"):
        seeds=line.split(':')[1].strip().split(' ')
    elif len(line.strip())!=0 and line[0].isdigit():
        sline = line.split(' ')
        #src dest range
        #seed to soil (seed = src, soil = dest)
        maps[a].append([int(sline[1]),int(sline[0]),int(sline[2])])
    elif len(line.strip())==0:
        a+=1


def lookup(_map, val):
    for i in range(len(_map)):
        if _map[i][0]<=val<=_map[i][0]+_map[i][2]:
            diff = _map[i][0]+_map[i][2] - val
            return _map[i][2] + _map[i][1] - diff
    return val

def location(maps, seed):
    for i in range(7):
        seed = lookup(maps[i], seed)
    return seed

def compute_range(maps, s_min, s_max):
    loc_max = location(maps, s_max)
    loc_min = location(maps, s_min)

    print(f's_min = {s_min} s_max = {s_max} loc_max = {loc_max} loc_min = {loc_min}')

    if loc_max-loc_min==s_max-s_min:
        return loc_min
    elif s_max-s_min==0:
        return loc_min
    else:
        s_med = int((s_max + s_min)/2)
        return min(compute_range(maps, s_min, s_med), compute_range(maps, s_med, s_max))


s=0
mins = []
while s+1<len(seeds):
    r = int(seeds[s+1]) - 1 
    seed_min = int(seeds[s])
    seed_max = seed_min + r

    mins.append(compute_range(maps, seed_min, seed_max))
    s+=2

print(min(mins))
