class String:
    s = ""

    def __init__(self):
        pass

    def get_string(self):
        self.s = input("String : ")

    def print_string(self):
        self.s = self.s.upper()
        print(self.s)


s1 = String()
s1.get_string()
s1.print_string()
