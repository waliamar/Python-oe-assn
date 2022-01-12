def char_freq(inp):
    dict = {}
    for i in inp:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict


print(char_freq("wabba lubba dub dub"))
