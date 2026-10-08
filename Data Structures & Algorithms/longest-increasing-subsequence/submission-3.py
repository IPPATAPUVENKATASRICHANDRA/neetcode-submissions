from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        @cache
        def dfs(i,j):
            if i==len(nums):
                return 0

            ans=dfs(i+1,j)

            if j==-1 or nums[j]<nums[i]:
                ans=max(ans,1+dfs(i+1,i))
            
            return ans
        
        return dfs(0,-1)
