class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        ans=[]
        def backtrack(st,cb_sum):

            if sum(cb_sum)==target:
                ans.append(cb_sum[:])
                return
            
            if sum(cb_sum)>target:
                return

            for i in range(st,len(candidates)):
                if i>st and candidates[i]==candidates[i-1]:
                    continue
                cb_sum.append(candidates[i])
                backtrack(i+1,cb_sum)
                cb_sum.pop()
        
        backtrack(0,[])

        return ans