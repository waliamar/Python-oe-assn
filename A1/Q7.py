inp = input("Enter desired numbers seperated by spaces : ")

a = inp.split()
sum = 0

for i in range(len(a)):
    if int(a[i]) < 101:
        sum += int(a[i])

print("The sum is : {}".format(sum))
