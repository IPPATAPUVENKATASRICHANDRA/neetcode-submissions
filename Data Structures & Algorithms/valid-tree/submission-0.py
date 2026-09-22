class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj=[[] for i in range(n)]

        for ed in edges:
            u,v=ed
            adj[u].append(v)
            adj[v].append(u)
        
        visit=set()
        def dfs(n,par):
            if n in visit:
                return False
            
            visit.add(n)

            for neigh in adj[n]:
                if neigh==par:
                    continue
                if not dfs(neigh,n):
                    return False
            
            return True
        
        return dfs(0,-1) and len(visit)==n



