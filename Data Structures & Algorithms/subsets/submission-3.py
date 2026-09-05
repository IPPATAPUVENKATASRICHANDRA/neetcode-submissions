class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        def backtrack(ans,i):
            res.append(ans[:])

            for j in range(i,len(nums)):
                ans.append(nums[j])
                backtrack(ans,j+1)
                ans.pop()
        
        backtrack([],0)

        return res
            