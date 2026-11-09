class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        mem={}
        def helper(cur):
            if cur==target:
                return 1
            
            if cur in mem:
                return mem[cur]
            
            if cur>target:
                return 0
                
            ans=0
            for i in nums:
                ans+=helper(cur+i)
            
            mem[cur]=ans

            return ans
            
        return helper(0)

            
            
            
                