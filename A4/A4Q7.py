from math import sqrt


def MySqrt(n):
    if n < 0:
        raise Exception("Number should not be -ve")
    return sqrt(n)


n = int(input("Type a number : "))
print(MySqrt())
