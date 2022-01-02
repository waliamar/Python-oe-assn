f = open("allprograms.txt", mode="a")

for i in range(2, 33):
    if i in (10, 13, 21, 31):
        continue
    name = "Q"+str(i)+".py"
    f = open(name, mode="r")
    xs = f.readlines()
    f.close()
    g = open("allprograms.txt", "a")
    g.write("\n\nQ {} \n\n".format(i))
    for v in xs:
        g.write(v)
    g.close()

for i in range(1, 23):
    if i in (8, 17, 20):
        continue
    name = "A2Q"+str(i)+".py"
    f = open(name, mode="r")
    xs = f.readlines()
    f.close()
    g = open("allprograms.txt", "a")
    g.write("\n\nA2Q {} \n\n".format(i))
    for v in xs:
        g.write(v)
    g.close()
