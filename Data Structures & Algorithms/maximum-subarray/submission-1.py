class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        if len(nums)==1:
            return nums[0]
        maxval=nums[0]
        cursum=0
        for i in nums:
            if cursum<0:
                cursum=0
            cursum+=i
            maxval=max(maxval,cursum)

        
        return maxval