class Sets:
    def sub_sets(self, sub):
        return self.subsetsRecur([], sorted(sub))

    def subsetsRecur(self, current, sub):
        if sub:
            return self.subsetsRecur(current, sub[1:]) + self.subsetsRecur(current + [sub[0]], sub[1:])
        return [current]


print(Sets().sub_sets([4, 5, 6]))
