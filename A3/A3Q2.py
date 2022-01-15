def getproducts(n):
    products = []
    item = []
    f = open("shopper_list.txt", "a+")
    for i in range(n):
        item = []
        s = input("Enter product details: ")
        f.write(s)
        f.write("\n")
        item.append(s)
        products.append(item)
    print(products)
    f.close()


n = int(input("Number of entries : "))
getproducts(n)
