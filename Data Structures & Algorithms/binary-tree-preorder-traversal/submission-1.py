# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans=[]
        def pre_traversal(root):
            if not root:
                return
            
            ans.append(root.val)
            pre_traversal(root.left)
            pre_traversal(root.right)
        
        pre_traversal(root)
        return ans
