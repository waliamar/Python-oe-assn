a = input("First string : ")
b = input("Second string : ")

s = b[:2]+a[2:] + " " + a[:2]+b[2:]
print(s)
