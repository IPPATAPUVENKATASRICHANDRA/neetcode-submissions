class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        mem={}
        def dfs(i,track):

            if track>amount or i>=len(coins):
                return 0
            
            if track==amount:
                return 1
            
            if (i,track) in mem:
                return mem[(i,track)]
            
            mem[(i,track)]=dfs(i,track+coins[i])+dfs(i+1,track)

            return mem[(i,track)]

        
        return dfs(0,0)
        



