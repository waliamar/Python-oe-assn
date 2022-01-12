def lines(file_name):
    f = open(file_name, mode="r")
    lst = f.readlines()
    return len(lst)


print(lines("test.txt"))
