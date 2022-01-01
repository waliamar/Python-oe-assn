def lst(l1, l2):
    result = False
    for i in l1:
        for j in l2:
            if i == j:
                result = True
    return result


print(lst([1, 2, 3], [4, 5, 6]))
print(lst([1, 2, 3], [4, 5, 6, 3]))
