# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_ht=self.maxHeight(root.left)
        right_ht=self.maxHeight(root.right)
        diameter=left_ht+right_ht
        temp1=self.diameterOfBinaryTree(root.left)
        temp2=self.diameterOfBinaryTree(root.right)

        return max(diameter,temp1,temp2)
        

    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))