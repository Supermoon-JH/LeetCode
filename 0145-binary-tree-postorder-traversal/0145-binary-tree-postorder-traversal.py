# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if not root:
            return result

        def dfs(node):
            if not node:
                return
            result.append(node.val)
            
            dfs(node.right)
            dfs(node.left)

        dfs(root)
        result.reverse()
        return result