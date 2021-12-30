a = input("First\n")
b = input("Second\n")
c = []
d = []

for i in a:
    if i != " ":
        c.append(i)

for i in b:
    if i != " ":
        d.append(i)

print(c)
print(d)

state = "False"

for i in c:
    if i in d:
        state = "True"
        break

print(state)
