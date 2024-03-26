class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_pair=[]
        for i in nums:
            temp_nums=nums.copy()
            temp_nums.remove(i)
            for x in temp_nums:
                if i+x==target:
                    num_pair.append(nums.index(i))
                    if i==x:
                        nums.remove(i)
                        num_pair.append((nums.index(x)+1))
                    else:    
                        num_pair.append(nums.index(x))
                    return num_pair
        return []