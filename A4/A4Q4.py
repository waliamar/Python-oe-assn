def readposint():
    while True:
        number = input("Enter a number: ")
        try:
            val = int(number)
            if val < 0:
                print("Type positive integer!!")
                continue
            break
        except ValueError:
            print("That's not an int!")
    print(val)


readposint()
