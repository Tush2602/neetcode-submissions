# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):
            if node is None:
                return 0
            
            left_ht = height(node.left)
            if left_ht == -1:
                return -1 
            right_ht = height(node.right)

            if right_ht == -1:
                return -1
            
            if abs(left_ht - right_ht) > 1:
                return -1
            return 1+ max(left_ht, right_ht)

        return height(root) != -1
        