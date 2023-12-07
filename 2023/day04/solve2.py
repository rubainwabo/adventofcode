import sys

input = open(sys.argv[1]).read().strip()

scores=[]
cards=[]
toadd=[]

for line in input.split('\n'):
    cards.append(1)
    toadd.append(1)
    data = line.split(':')[1].strip().split('|')
    pts = data[0].strip().split(' ')
    nbrs = data[1].strip().split(' ')

    score=0
    for nbr in nbrs:
        for pt in pts:
            if pt.isdigit() and nbr.isdigit():
                if pt == nbr:
                    score += 1
    scores.append(score)
    
for i in range(len(scores)):
    score = scores[i]
    for j in range(i+1, len(cards)):
        if score<=0:
            break
        cards[j]+=toadd[i]
        score-=1
    if i+1<len(toadd):
        toadd[i+1]=cards[i+1]
total=0
for i in range(len(cards)):
    total+=cards[i]
print(total)