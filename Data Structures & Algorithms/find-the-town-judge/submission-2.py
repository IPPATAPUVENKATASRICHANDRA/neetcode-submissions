class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        d=[[0]*(n+1) for _ in range(n+1)]
        
        for u,v in trust:
            d[u][v]=1
        print(d)
        for c in range(len(d)):
            col_values = [row[c] for row in d]
            print(col_values)
            if sum(col_values)==n-1 and sum(d[c])==0:
                return c
        return -1
