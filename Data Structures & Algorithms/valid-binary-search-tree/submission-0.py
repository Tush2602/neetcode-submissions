# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def bst(root, minm, maxm):
            if root is None:
                return True
            if not (minm < root.val < maxm):
                return False
            if root.left:
                if not (minm < root.left.val < root.val):
                    return False 
            if root.right:
                if not (root.val < root.right.val < maxm):
                    return False

            if not (bst(root.left, minm, maxm = root.val)):
                return False
            if not (bst(root.right, minm = root.val, maxm=maxm)):
                return False

            return True

        return bst(root, minm = float("-inf") , maxm = float("inf"))
        