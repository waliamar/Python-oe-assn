for i in range(1, 17):
    try:
        f = open("A4Q"+str(i)+".py", mode="x")
    except:
        FileExistsError
