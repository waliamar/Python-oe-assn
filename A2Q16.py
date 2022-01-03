s = input("String : ")
done = {}
count = 0
for i in s:
    if i in done:
        done[i] += 1
    else:
        done[i] = 1
for key, value in done.items():
    print(key, value, sep=",", end=" ")
