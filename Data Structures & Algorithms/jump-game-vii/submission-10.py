class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        if s[-1] == '1':
            return False
        n=len(s)

        dp=[False]*n
        dp[0]=True
        cnt=0 # no of reachable positions with [i-minjump,i-maxjump]
        # window: i-maxJump<= k<= i -minJump
        for i in range(1,n):
            # entering the window
            if i>=minJump and dp[i-minJump]:
                cnt+=1
            
            # leaving the window
            if i>=maxJump and dp[i-maxJump-1]:
                cnt-=1
            
            if cnt>0 and s[i]=='0':
                dp[i]=True
        
        return dp[n-1]

