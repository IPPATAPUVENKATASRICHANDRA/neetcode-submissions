class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        dp={}
        def dfs(l,r):
            if l>r:
                return 0
            # when alice taking a pile the whole piles will be even 
            if (l,r) in dp:
                return dp[(l,r)]
            ev=(r-l+1)%2==0
            l_val=piles[l] if ev else 0
            r_val=piles[r] if ev else 0

            dp[(l,r)]= max(dfs(l+1,r)+l_val,dfs(l,r-1)+r_val)

            return dp[(l,r)]
        
        total=sum(piles)
        alice=dfs(0,len(piles)-1)
        return True if alice>total-alice else False
