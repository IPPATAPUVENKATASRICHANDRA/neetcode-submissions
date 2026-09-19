class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        mem={}
        def helper(i):
            if i>=len(cost):
                return 0
            
            if i in mem:
                return mem[i]
            
            mem[i]=cost[i]+min(helper(i+1),helper(i+2))
            return mem[i]

        return min(helper(0),helper(1))

