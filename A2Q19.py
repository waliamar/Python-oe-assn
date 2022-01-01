def count_values(dic):
    value = []
    count = 0
    for i in dic.values():
        if i not in value:
            count += 1
            value.append(i)
    return count


print(count_values({'red': 1, 'green': 1, 'blue': 2}))
