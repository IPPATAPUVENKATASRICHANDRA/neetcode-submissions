class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        mem={}
        def helper(ongoing_val,i):

            if i==len(nums):
                return 1 if ongoing_val==target else 0
            
            if (ongoing_val,i) in mem:
                return mem[(ongoing_val,i)]

            # ongoing_val +/- nums[i]

            mem[(ongoing_val,i)] = (helper(ongoing_val+nums[i],i+1)
            + helper(ongoing_val-nums[i],i+1)
)
            return mem[(ongoing_val,i)]

    
        return helper(0,0)

    

