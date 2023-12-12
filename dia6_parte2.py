times = [48989083]
distance = [390110311121360]

total = 1

for x in range(len(times)):
    contador = 0
    for i in range(times[x]):
        print(i)
        if (times[x] - i) * i > distance[x]:
            contador += 1
    if (contador > 0): total = total * contador

print(total)
