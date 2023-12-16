import sys
import functools

input = open(sys.argv[1]).read().strip().split('\n')

t = [x.split(' ')[0] for x in input]
b = [int(x.split(' ')[1]) for x in input]
d = {'A': 0,'K': 1,'Q': 2,'J': 3,'T': 4,'9': 5,'8': 6,'7': 7,'6': 8,'5': 9,'4': 10,'3': 11,'2': 12, 'J':13}

"""
    'Five of a kind': 7,
    'Four of a kind': 6,
    'Full house': 5,
    'Three of a kind': 4,
    'Two pair': 3,
    'One pair': 2,
    'Highest card': 1
"""

def get_hand(x):
    c = [0]*14
    for xx in x:
        c[d[xx]]+=1
    j = c[13]
    c[13]=0 
    c.sort()
    c.reverse()
    if c[0]==5 or j==5:
        return 7
    elif c[0]==4:
        if j==1: return 7
        return 6
    elif c[0]==3 and c[1]==2:
        return 5
    elif c[0]==3:
        if j==2: return 7
        elif j==1: return 6
        return 4
    elif c[0]==2 and c[1]==2:
        if j==1: return 5
        return 3
    elif c[0]==2:
        if j==3: return 7
        elif j==2: return 6
        elif j==1: return 4
        return 2
    else:
        if j==4: return 7
        elif j==3: return 6
        elif j==2: return 4
        elif j==1: return 2
        return 1 

def compare(x,y):
    h_x = get_hand(x)
    h_y = get_hand(y)
    if (h_x-h_y)==0:
        for i in range(len(x)):
            if d[x[i]]>d[y[i]]:
                return -1
            elif d[x[i]]<d[y[i]]:
                return 1
        return 0
    return h_x-h_y

sorted_t = sorted(t, key=functools.cmp_to_key(lambda x,y: compare(x,y)))

s = 0
for i in range(len(sorted_t)):
    s+=b[t.index(sorted_t[i])]*(i+1)
print(s)
    
    
    