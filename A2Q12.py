
def unique_list(l):
    a = []
    for i in l:
        if i not in a:
            a.append(i)
    return a


l = [1, 2, 3, 3, 3, 3, 4, 5]
print("Sample list : "+str(l))
print("Unique list : "+str(unique_list(l)))
