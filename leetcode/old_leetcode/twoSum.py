class Solution():
    def __init__(self):
        self.twoSum([3, 3], 6)

    def twoSum(self, nums, target):
        self.copyList=nums.copy()
        for i in nums:
            self.copyList.remove(i)
            for x in self.copyList:
                if i+x==target:
                    self.firstIndex=nums.index(i)
                    nums.remove(i)
                    self.secondIndex=nums.index(x)+1

        self.twoNumbers=[self.firstIndex, self.secondIndex]
        return self.twoNumbers


instance=Solution()

# two of the same number can come up, though they will be different items in the list