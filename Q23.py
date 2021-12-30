c = float(input("Type celsius value : "))
f = float(input("Type fahrenheit value : "))

print(" {} C is {:.2f} in Fahrenheit".format(c, (c/5)*9+32), end=".")
print(" {} F is {:.2f} in Celsius".format(f, ((f-32)/9)*5, end="."))
