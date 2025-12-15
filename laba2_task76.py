import requests
import matplotlib.pyplot as plt

def ras(k):
    data = k.split(',')
    return data

f = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/opendata.stat")
lst = list(map(ras, str(f.text).split('\n')[1:])) 
pensia = []
for i in lst:
    try:
        if i[0] == 'Средняя пенсия' and i[1] == 'Забайкальский край' and i[2][:4] == '2018':
            pensia.append([i[2], int(i[3])])
    except:
        pass
summa = sum([i1[1] for i1 in pensia])
print("Срендяя пенсия в 2018:",summa/len(pensia))

dates = [term[0] for term in pensia]
values = [term[1] for term in pensia]

plt.figure(figsize=(12, 6))
plt.plot(dates, values)

plt.title('Средний размер пенсии по месяцам в Забайкальском крае в 2018')
plt.xlabel('Дата')
plt.ylabel('Средний размер пенсии')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
