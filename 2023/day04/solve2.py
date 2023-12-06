import sys

input = open(sys.argv[1]).read().strip()

scores=[]
cards=[]

for line in input.split('\n'):
    cards.append(1)
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

print('scores:', scores)

print('cards before:', cards)

for i in range(len(scores)):
    score = scores[i]
    print('cards step:', cards)
    for j in range(i+1, len(cards)):
        if score<=0:
            break
        cards[j]+=1
        score-=1
print('cards:', cards)