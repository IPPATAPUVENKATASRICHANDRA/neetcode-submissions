class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        nums.sort()
        ans=0
        mod=10**9+7
        r=len(nums)-1

        for l,val in enumerate(nums):

            while l<=r and val+nums[r]>target:
                r-=1
            
            if l<=r:
                ans+=pow(2,r-l)
                ans%=mod
        return ans