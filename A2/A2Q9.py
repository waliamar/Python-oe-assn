dict1 = {'a': 1, 'b': 2, 'c': 4, 'd': 8}
dict2 = {'e': 16, 'c': 4, 'f': 12}

print("Dict 1 : ", dict1)
print("Dict 2 : ", dict2)


def dict_intersect(dict1, dict2):
    dictcomn = {}
    for i in dict1:
        if i in dict2:
            if dict1[i] == dict2[i]:
                dictcomn = {i: dict2[i]}
    return dictcomn


print("Result : ", dict_intersect(dict1, dict2))
