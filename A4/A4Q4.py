def readposint():
    while True:
        number = input("Enter a number: ")
        try:
            val = int(number)
            if val < 0:
                print("Sorry, input must be a positive integer, try again")
                continue
            break
        except ValueError:
            print("That's not an int!")
    print(val)


readposint()
