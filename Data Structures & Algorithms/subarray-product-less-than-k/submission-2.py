class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
         
        l=0
        val=1
        ans=0

        for r in range(len(nums)):
            val*=nums[r]
            while l<=r and val>=k:
                val/=nums[l]
                l+=1
            
            ans+=(r-l+1)

        return ans