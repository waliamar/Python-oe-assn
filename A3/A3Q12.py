def file_read(fname):
    f = open(fname)
    content_list = f.readlines()
    print(content_list)


file_read('test.txt')


def longest_word(filename):
    f = open(filename, 'r')
    words = f.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]


print(longest_word('test.txt'))
