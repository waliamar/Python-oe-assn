def gen_dict():
    a = {}
    for i in range(1, 21):
        a[i] = i**2
    print(list(a.keys()))


gen_dict()
