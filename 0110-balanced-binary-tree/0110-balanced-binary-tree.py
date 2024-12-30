# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.check(root) != -1
    
    def check(self, root):
        if root is None:
            return 0
        
        left_height = self.check(root.left)
        if left_height == -1:
            return -1
        
        right_height = self.check(root.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1