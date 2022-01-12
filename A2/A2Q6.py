vowels = "aeiouAEIOU"

a = input("String : ")
c = 0
for i in a:
    if i in vowels:
        c += 1
print(c)
