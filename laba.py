f=open('sport (1).txt', encoding='cp1251')
f.readline()
sports = {}
for line in f.readlines():
    types = str(line.split("\t")[3]).split(',')

    if types!=[""]:
        for curr in types:
            curr = curr.strip()
            if curr not in sports: sports[curr] = 1
            else: sports[curr] += 1

sports = sorted(sports.items(), key=lambda item: item[1], reverse = True)
for i in range (3):
    print(f"{sports[i][0]}-{str(sports[i][1])}")
