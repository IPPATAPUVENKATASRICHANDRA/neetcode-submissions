class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans=[]

        def backtrack(per,rem):
            if len(per)==len(nums):
                ans.append(per[:])
                return
            
            for i in range(len(rem)):
                per.append(rem[i])
                backtrack(per,rem[:i]+rem[i+1:])
                per.pop()
        
        backtrack([],nums)

        return ans