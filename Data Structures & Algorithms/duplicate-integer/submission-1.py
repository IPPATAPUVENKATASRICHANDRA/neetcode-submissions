
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums)<=0:
            return False
        
        if len(nums)==1:
            return False

        hash_set=set()
        for i in nums:
            if i in hash_set:
                return True
            else:
                hash_set.add(i)

        return False 
    