row = input("Type the number of rows \n")
column = input("Type the number of columns \n")

a = []

for i in range(0, int(row)):
    b = []
    for j in range(0, int(column)):
        b.append(i*j)
    a.append(b)
print(a)
