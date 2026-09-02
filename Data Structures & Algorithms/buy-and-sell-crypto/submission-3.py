class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # max_val=0
        # for i in range(len(prices)-1):
        #     for j in range(i+1,len(prices)):
        #         val=prices[j]-prices[i]
        #         max_val=max(max_val,val)
        
        # return max_val

        l,r=0,1
        max_val=0

        while l<=r and r<=len(prices)-1:
            if prices[l]<=prices[r]:
                max_val=max(max_val,prices[r]-prices[l])
            else:
                l=r
            r+=1
        
        return max_val
