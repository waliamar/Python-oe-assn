count = 0


def takeinp():
    global full
    full = []
    full = list(input("Enter binary number\n"))


takeinp()

for i in full:
    if i != '0' and i != '1':
        print("\u001b[31m Error : String not in binary format \n \u001b[0m" +
              "Type only 1's and 0's.")
        takeinp()
        break
full_rev = (full[::-1])
for i in range(len(full_rev)):
    count += (2**i)*int(full_rev[i])

print("Number = " + str(count))
