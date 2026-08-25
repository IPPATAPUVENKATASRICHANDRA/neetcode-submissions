class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        unq=set()
        for i in range(len(nums)):
            if nums[i] not in unq:
                unq.add(nums[i])
            
            else:
                return True
        
        return False