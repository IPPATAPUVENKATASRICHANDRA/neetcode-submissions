class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)

        ans=low

        while low<=high:
            mid=(low+high)//2

            if self.checker(nums,mid,k):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        
        return ans
    
    def checker(self,nums,mid,k):
        cnt=1
        val=0
        for i in nums:
            val+=i
            if val>mid:
                cnt+=1
                val=i
        
        return cnt<=k