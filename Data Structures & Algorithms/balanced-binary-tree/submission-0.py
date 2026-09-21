# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def ht(node):
            if node is None:
                return 0
            left_ht = ht(node.left)
            right_ht =ht(node.right)

            return 1 + max(left_ht, right_ht)

        if root is None:
            return True

        if abs(ht(root.left) - ht(root.right)) > 1:
            return False
    
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        