one = int(input("Enter the number of ₹1 coins : "))
two = int(input("Enter the number of ₹2 coins : "))
five = int(input("Enter the number of ₹5 coins : "))
ten = int(input("Enter the number of ₹10 coins : "))
print("The total amount is ₹", end="")

total = one+two*2+five*5+ten*10

print(total)
