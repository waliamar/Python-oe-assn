a = input("Type comma seperated numbers:").split(",")
try:
    result = (int(a[0])/int(a[1]))
    try:
        pass
    finally:
        print(result)
except ZeroDivisionError:
    print("Denominator should not be zero")
except ValueError:
    print("Given values are not integers")
