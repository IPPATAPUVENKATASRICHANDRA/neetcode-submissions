"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # return deepcopy(node)

        clone_track={}

        def dfs(node):
            if node in clone_track:
                return clone_track[node]
            
            copy=Node(node.val)
            clone_track[node]=copy

            for i in node.neighbors:
                copy.neighbors.append(dfs(i))
            
            return copy
        

        return dfs(node) if node else None