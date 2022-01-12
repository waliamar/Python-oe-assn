a = "yahoo.com"

x = []
count = 0

for i in a:
    if i in x:
        count += 1
        continue
    temp = i
    count += 1
    x.append(i)

counter = 0
y = []

for i in x:
    for j in a:
        if (i == j):
            counter += 1
    y.append(i+" : "+str(counter))
    counter = 0

for i in y:
    print(i)
