
f = open("original_text.txt", "r")
data = f.read()

count = 0
for c in data:
    if c == 'c' or c == "C":
        count += 1

print(count)
