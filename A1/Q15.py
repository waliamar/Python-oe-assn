a = []
count = 0
for i in range(100, 401):
    for j in str(i):
        if int(j) % 2 != 0:
            count += 1
        if count == 3:
            a.append(i)
    count = 0
for b in a:
    print(b, end=",")
