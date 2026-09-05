class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        l=0
        max_ans=1
        nums=sorted(set(nums))
        for r in range(len(nums)):
            if nums[r]!=nums[r-1]+1:
                l=r
            
            max_ans=max(max_ans,r-l+1)
        
        return max_ans

            

        
