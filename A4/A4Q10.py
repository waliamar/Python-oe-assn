class MyClass:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(MyClass().reverse_words('hello .py'))
