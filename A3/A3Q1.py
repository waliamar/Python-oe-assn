f = open("test.txt", "r")
data = f.read()
f.close()
lines = data.split("\n")
for line in lines:
    line = line.rstrip()
    line = line.lower()
lines.sort()
for entry in lines:
    print(entry)
