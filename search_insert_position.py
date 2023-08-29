import logging
logging.basicConfig(level=logging.DEBUG)

class Solution:
    def __init__(self) -> None:
        self.searchInsert([1, 3, 5, 6], 0)

    def searchInsert(self, nums: int, target: int)-> int:
        logging.debug(target)
        logging.debug(nums)


        if target in nums:
            logging.debug("target in nums")
            for i in nums:
                if i==target:
                    target_index=nums.index(i)
                    logging.debug(target_index)
                    return target_index
        elif target>nums[-1]:
            target_index=len(nums)
            return target_index
        else:
            logging.debug("target is not in nums")
            for i in nums:
                    if i>target:
                        target_index=nums.index(i)
                        logging.debug(nums)
                        logging.debug(i)
                        logging.debug(target_index)
                        return target_index



instance=Solution()
