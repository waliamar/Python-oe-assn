n = int(input("Type a number : "))
s = ""
while n != 0:
    if(n % 2) == 0:
        s += "0"
    else:
        s += "1"
    n = n//2
if n == 0:
    s += "0"
print("Binary number : " + s[::-1])
