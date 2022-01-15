fibo = [0, 1]

i = 1
while True:
    if (fibo[i-1]+fibo[i] < 50):
        fibo.append(fibo[i-1] + fibo[i])
    else:
        break
    i += 1

print(fibo)
