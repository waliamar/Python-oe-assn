def prime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2, n):
            if(n % x == 0):
                return False
        return True


prime_numbers = []
numbers = [int(b) for b in input("list : ").split()]
for i in numbers:
    if prime(i):
        prime_numbers.append(i)

print("Prime numbers :", prime_numbers)
