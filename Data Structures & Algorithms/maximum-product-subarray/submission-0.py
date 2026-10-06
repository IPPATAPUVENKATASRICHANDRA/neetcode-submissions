class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        ans=nums[0]
        curmin,curmax=1,1

        for i in nums:
            temp=curmax*i
            curmax=max(curmax*i,curmin*i,i)
            curmin=min(temp,curmin*i,i)
            ans=max(ans,curmax)
        
        return ans
