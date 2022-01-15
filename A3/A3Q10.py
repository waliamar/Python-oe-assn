from time import daylight


f = open("test.txt", "r")
data = f.readlines()

print(data)
f.close()
g = open("result.txt", "w")
g.writelines(data[::-1])
g.close()
