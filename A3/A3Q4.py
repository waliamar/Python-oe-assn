f = open("test.txt", "r")
data = f.readlines()
f.close()

data.sort()

g = open("result.txt", "w")
g.writelines(data)
g.close()
