def string_test(s):
    d = {"upr": 0, "lwr": 0}
    for c in s:
        if c.isupper():
            d["upr"] += 1
        elif c.islower():
            d["lwr"] += 1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upr"])
    print("No. of Lower case Characters : ", d["lwr"])


string_test('The quick Brown Fox')
