import logging
from operator import index
from os import remove
logging.basicConfig(level=logging.DEBUG)


class Solution:
    def __init__(self):
        self.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    
    """
    k is the length of the numbers left after the duplicates have been removed
    
    i cannot use a second array and so should modify the original one and keep a record of the 
    length so i can add the underscores at t1,1,2]he end

    """

    def removeDuplicates(self, nums) -> int:
        if len(nums)==0:
            return 0
        k=1
        index=1
        previous=nums[0]
        for i in range(1, len(nums)):
            if nums[i]!=previous:
                k+=1
                previous=nums[i]
                nums[index]=nums[i]
                index+=1
        return k


