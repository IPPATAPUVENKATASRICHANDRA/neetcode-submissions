import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k=[0,max(piles)] 
        l=1
        r=max(piles)
        ans=max(piles)
        while l<=r:
            mid=(l+r)//2
            total_time=0
            for i in piles:
                total_time+=math.ceil(i/mid)
            
            if total_time<=h:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        
        return ans

