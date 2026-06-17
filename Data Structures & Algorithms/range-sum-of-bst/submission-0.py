# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
         
        val=0
        def helper(node):
            nonlocal val
            if node is None:
                return 0
            
            if low<=node.val<=high:
                val+=node.val
            
            helper(node.left)
            helper(node.right)
        
        helper(root)

        return val


    