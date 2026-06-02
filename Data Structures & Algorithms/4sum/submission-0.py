class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans=[]
        nums.sort()

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                l=j+1
                r=len(nums)-1

                while l<r:
                    val=nums[i]+nums[j]+nums[l]+nums[r]
                    if val==target:
                        tem=[nums[i],nums[j],nums[l],nums[r]]
                        if tem not in ans:
                            ans.append(tem)
                    
                    if val<target:
                        l+=1
                    else:
                        r-=1
        
        return ans
                    
                    
                    
