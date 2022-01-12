from random import randrange


def ran(start, end=0):
    if not end:
        end = start
        start = 0
    print(randrange(start, end, 2))


ran(100)
