class Solution:
    def findMin(self, nums: List[int]) -> int:

        l=0
        r=len(nums)-1
        min_val=1
        while l<=r:
            if nums[r]<nums[l]:
                l=l+1
                min_val=nums[r]
            
            else:
                r=r-1
                min_val=nums[l]
        
        return min_val
