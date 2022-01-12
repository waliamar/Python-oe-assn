def four(a):
    count = 0
    for i in a:
        if i == 4:
            count += 1
    return count


print(four([1, 4, 6, 7, 4]))
