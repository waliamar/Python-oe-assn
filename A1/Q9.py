# a = 0
# b = 1
# fib = [0, 1]
# i = 0

# while fib[i] < 50:
#     c = a+b
#     fib.append(c)
#     a = b
#     b = c
#     i += 1

# print(fib)

fibo = [0, 1]

i = 1
while True:
    if (fibo[i-1]+fibo[i] < 50):
        fibo.append(fibo[i-1] + fibo[i])
    else:
        break
    i += 1

print(fibo)
