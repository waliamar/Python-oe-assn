def fun():
    n = int(input("length n : "))
    strng = input("string : ")
    result = []
    words = strng.split(" ")
    for i in words:
        if len(i) > n:
            result.append(i)
    return result


print(fun())
