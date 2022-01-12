a = []
for i in range(1, 10):
    a.append("*"*(5-abs(i-5)))
print("\n".join(a))
