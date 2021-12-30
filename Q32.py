s = input("String : ")
skip = 0
for i in range(1, len(s)):
    if s[i] == s[0]:
        s = s[:i]+"$"+s[i+1:]
print(s)
