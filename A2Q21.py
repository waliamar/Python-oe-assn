def sort(s):
    a = s.split(" ")
    for i in range(len(a)):
        a[i] = a[i].lower()
    a.sort()
    print(" ".join(a))


sort("Ayo bruv wassup how you doin")
