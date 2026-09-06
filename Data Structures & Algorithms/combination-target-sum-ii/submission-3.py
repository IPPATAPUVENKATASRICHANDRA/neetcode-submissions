class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res=[]
        candidates.sort()

        def bt_cs2(ans,i,total):


            if total == target:
                res.append(ans[:])
                return

            for j in range(i, len(candidates)):

                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                if total + candidates[j] > target:
                    break

                ans.append(candidates[j])
                bt_cs2(ans, j + 1, total + candidates[j])
                ans.pop()

        
        bt_cs2([],0,0)

        return res