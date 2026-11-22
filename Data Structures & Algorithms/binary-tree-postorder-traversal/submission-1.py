# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans=[]
        def pst_traversal(root):
            if not root:
                return 
            pst_traversal(root.left)
            pst_traversal(root.right)
            ans.append(root.val)
        
        pst_traversal(root)
        return ans
            
