# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def goodnode(node, maxm = root.val):
            if node is None:
                return 0
            
            if node.val >= maxm:
                good=1
            else: 
                good = 0
            left_count = goodnode(node.right, max(node.val, maxm))
            right_count = goodnode(node.left, max(node.val, maxm))

            return good + left_count + right_count

        return goodnode(root)

        
        

        
        