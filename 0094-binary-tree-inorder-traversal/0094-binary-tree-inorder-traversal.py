# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.travel(root, result)
        
        return result

    def travel(self, root, result):
        if root is not None:
            self.travel(root.left, result)
            result.append(root.val)
            self.travel(root.right, result)
            
        