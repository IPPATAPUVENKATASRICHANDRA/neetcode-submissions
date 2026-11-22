# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans=[]

        def in_t(root):
            if not root:
                return 

            in_t(root.left)
            ans.append(root.val)
            in_t(root.right)
        
        in_t(root)
        return ans