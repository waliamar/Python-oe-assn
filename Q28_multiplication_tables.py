num = int(input("Type the number you want tables of : "))

for i in range(10):
    print("{} X {} = {}".format(num, i+1, (num*int(i+1))))
