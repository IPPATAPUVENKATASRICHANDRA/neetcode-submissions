class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_val=0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                val=prices[j]-prices[i]
                max_val=max(max_val,val)
        
        return max_val

