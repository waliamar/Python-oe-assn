def getentries(n):
    f = open("phonebook.txt", "a+")
    print("type contacts with numbers")
    for i in range(n):
        contact = input("Enter contact {} : ".format(i+1))
        f.write(contact)
        f.write("\n")
    f.close()


n = int(input("Type the number of entries : "))
getentries(n)
f = open("phonebook.txt", "r")
data = f.readlines()
data.sort()
f.close()
f = open("phonebook.txt", "w")
for i in data:
    f.write(i)
f.close()
