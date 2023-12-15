import sys
import time

start = time.time()


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

"""
                                        OBSERVATION :

Sometimes [seed_min, seed_max] with a range x will be mapped to [location_min, location_max] with
the same range x.

If that's the case we can skip all the calculations and just return location_min as the minimal location of [seed_min, seed_max].
Using binary search can help speeding up the process.
"""

def compute_interval(maps, s_min, s_max):
    loc_max = location(maps, s_max)
    loc_min = location(maps, s_min)

    if loc_max-loc_min==s_max-s_min or s_max-s_min==0:
        return loc_min
    else:
        s_med = int((s_max + s_min)/2)
        loc_med = location(maps, s_med)
        return min(loc_med, compute_interval(maps, s_min, s_med-1), compute_interval(maps, s_med+1, s_max))


s=0
mins = []
while s+1<len(seeds):
    r = int(seeds[s+1]) - 1 
    seed_min = int(seeds[s])
    seed_max = seed_min + r

    mins.append(compute_interval(maps, seed_min, seed_max))
    s+=2

end = time.time()
print(f'result : {min(mins)} in {end-start} seconds')
