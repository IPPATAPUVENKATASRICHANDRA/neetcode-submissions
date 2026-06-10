# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        t1=self.tracker(p)
        t2=self.tracker(q)
        print(t1,t2)
        if t1==t2:
            return True
        else:
            return False
    
    def tracker(self,root):
        if not root:
            return [None]
        
        else:
        
            return [root.val] + self.tracker(root.left) + self.tracker(root.right)