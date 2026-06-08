# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            new_val = self.next_val(root)
            root.val = new_val.val

            root.right = self.deleteNode(root.right, new_val.val)

        return root


    def next_val(self,root):
        cur = root.right

        while cur is not None and cur.left is not None:
            cur = cur.left

        return cur
