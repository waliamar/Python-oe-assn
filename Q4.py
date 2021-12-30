s1 = int(input("Type length of side 1 : "))
s2 = int(input("Type length of side 2 : "))
s3 = int(input("Type length of side 3 : "))

print("The triangle is of Type : ", end="")

if s1 == s2 and s2 == s3:
    print("Equilateral")
elif s1 != s2 and s2 != s3 and s3 != s1:
    print("Scalene")
else:
    print("Isoceles")
