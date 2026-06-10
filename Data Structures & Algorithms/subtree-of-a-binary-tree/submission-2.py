# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None:
            return False
        
        elif self.tracker(root)==self.tracker(subRoot):
            return True
        else:
            return(self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
    

    def tracker(self, root):
        if root is None:
            return [None]

        return [root.val] + self.tracker(root.left) + self.tracker(root.right)