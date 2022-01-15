class numbers:
    def sum(self, a, target):
        nums = {}
        for i, num in enumerate(a):
            if target - num in nums:
                return (nums[target - num], i)
            nums[num] = i


print("index1=%d, index2=%d" % numbers().sum((10, 20, 10, 40, 50, 60, 70), 50))
