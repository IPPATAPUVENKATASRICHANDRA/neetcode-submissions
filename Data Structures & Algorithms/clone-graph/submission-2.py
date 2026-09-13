"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        adj_list = {}

        def dfs(no):
            if no in adj_list:
                return adj_list[no]

            cp = Node(no.val)
            adj_list[no] = cp

            for n in no.neighbors:
                cp.neighbors.append(dfs(n))

            return cp

        return dfs(node) if node else None