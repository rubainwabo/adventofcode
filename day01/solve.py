dic = {
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}
som1 = 0
som2 = 0
with open('./input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        part1=[]
        part2=[]
        for i in range(len(line)):
            if (ord(line[i])>=48 and ord(line[i])<=57):
                part1.append(line[i])
                part2.append(line[i])
            else:
                for k, v in dic.items():
                    if line[i:].startswith(k):
                        part2.append(v)
        som1 += int(part1[0] + part1[-1])
        som2 += int(part2[0] + part2[-1])
print(som1)
print(som2)