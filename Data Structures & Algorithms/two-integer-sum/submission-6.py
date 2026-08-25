class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        # l=0
        # r=len(nums)-1

        # while l<=r:
        #     add=nums[l]+nums[r]
        #     if add==target:
        #         return [l,r]
            
        #     elif add>target:
        #         r-=1
        #     else:
        #         l+=1
        
        if len(nums)<=0:
            return []

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        