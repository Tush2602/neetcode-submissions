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
        result = 0
        def goodnode(node, maxm = root.val):
            nonlocal result
            if node is None:
                return 
            
            if node.val >= maxm:
                result+=1
            goodnode(node.right, max(node.val, maxm))
            goodnode(node.left, max(node.val, maxm))

        goodnode(root)
        return result

        
        

        
        