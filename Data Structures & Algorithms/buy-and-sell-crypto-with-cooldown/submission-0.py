from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @lru_cache(maxsize=None)
        def dfs_maxprof(i,hold):

            if i>=len(prices):
                return 0
            
            skip=dfs_maxprof(i+1,hold)
            if hold:
                sell=prices[i]+dfs_maxprof(i+2,False)
                return max(sell,skip)
            
            else:
                buy=-prices[i]+dfs_maxprof(i+1,True)
                return max(buy,skip)
        
        return dfs_maxprof(0,False)

            

