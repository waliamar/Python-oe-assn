class String:
    s = ""

    def __init__(self):
        pass

    def get_String(self):
        self.s = input("String : ")

    def print_String(self):
        self.s = self.s.upper()
        print(self.s)


s1 = String()
s1.get_String()
s1.print_String()
