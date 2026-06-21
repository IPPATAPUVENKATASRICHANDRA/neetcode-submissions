class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans=[]
        def backtrack(st,subar):
            if len(subar)==k:
                ans.append(subar[:])
            
            else:
                for i in range(st,n+1):
                    subar.append(i)
                    backtrack(i+1,subar)
                    subar.pop()
        

        backtrack(1,[])

        return ans
        