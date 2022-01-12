# Python code to remove duplicate elements
def dupe(lst):
    a = []
    for i in lst:
        if i not in a:
            a.append(i)
    return a


lst = [2, 4, 10, 20, 5, 2, 20, 4]
print(dupe(lst))
