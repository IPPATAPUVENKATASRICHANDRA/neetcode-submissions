class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)  


        l=0
        r=len(nums)-1
        ans=nums[0]

        while l<=r:
            mid=(l+r)//2
            ans=min(nums[mid],ans)

            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid-1
        
        return ans
            

            
