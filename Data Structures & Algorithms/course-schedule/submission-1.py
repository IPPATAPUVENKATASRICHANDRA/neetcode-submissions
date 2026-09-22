class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj=[[]for _ in range(numCourses)]

        for e in prerequisites:
            u,v=e
            adj[v].append(u)
        
        visiting = set()
        visited = set()

        def dfs(node):

            # cycle detected
            if node in visiting:
                return False

            # already checked before
            if node in visited:
                return True

            visiting.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False

            visiting.remove(node)
            visited.add(node)

            return True

        for n in range(numCourses):
            if not dfs(n):
                return False
        
        return True
                    
                    
                