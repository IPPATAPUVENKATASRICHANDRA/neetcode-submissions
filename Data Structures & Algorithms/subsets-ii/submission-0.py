class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans=set()
        nums.sort()

        def backtrack(st,ss):

            if tuple(ss) not in ans:
                ans.add(tuple(ss))
            
            for i in range(st,len(nums)):
                ss.append(nums[i])
                backtrack(i+1,ss)
                ss.pop()

        backtrack(0,[])
        
        return [list(i) for i in ans]