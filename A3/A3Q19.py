f = open("test.txt", "r")
data = f.readlines()
f.close()

for lines in data:
    if "msrit" in lines.lower():
        print(lines)
