class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit=set()
        adj_list=[[] for _ in range(n)]
        cnt=0
        for e in edges:
            u,v=e
            adj_list[u].append(v)
            adj_list[v].append(u)
        

        def dfs(n):
            for neigh in adj_list[n]:
                if neigh not in visit:
                    visit.add(neigh)
                    dfs(neigh)
        
        for i in range(n):
            if i not in visit:
                visit.add(i)
                dfs(i)
                cnt+=1

        return cnt
