# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.reverse(root.left, root.right, 0)

        return root

    def reverse(self, left, right, level):
        if left is None or right is None:
            return

        if level % 2 == 0:
            tmp = left.val
            left.val = right.val
            right.val = tmp
        
        self.reverse(left.left, right.right, level + 1)
        self.reverse(left.right, right.left, level + 1)