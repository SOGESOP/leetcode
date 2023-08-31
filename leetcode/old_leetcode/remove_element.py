import logging
logging.basicConfig(level=logging.DEBUG)

class Solution:
    def __init__(self) -> None:
        self.removeElement([3,2,2,3], 3)


    def removeElement(self, nums, val):
        index=0
        length=0
        for i in range (0, len(nums)):
            if nums[i]!=val:
                nums[index]=nums[i]
                index+=1
                length+=1
        return length

instance=Solution()