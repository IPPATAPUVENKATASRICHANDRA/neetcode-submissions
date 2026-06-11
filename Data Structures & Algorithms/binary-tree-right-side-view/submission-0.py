# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        stack = [(root, 0)]
        rightmost = {}

        while stack:
            node, depth = stack.pop()

            # overwrite with the latest node seen at this depth
            rightmost[depth] = node.val

            if node.right:
                stack.append((node.right, depth + 1))

            if node.left:
                stack.append((node.left, depth + 1))


        return [rightmost[d] for d in sorted(rightmost)]






            



            




