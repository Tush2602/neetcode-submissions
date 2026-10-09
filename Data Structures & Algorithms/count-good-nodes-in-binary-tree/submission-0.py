# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return []
        result = []
        def goodnode(node, result, maxm = root.val):
            if node is None:
                return 
            
            if node.val >= maxm:
                result.append(node.val)
            goodnode(node.right, result, max(node.val, maxm))
            goodnode(node.left, result, max(node.val, maxm))

        goodnode(root, result)
        return len(result)

        
        

        
        