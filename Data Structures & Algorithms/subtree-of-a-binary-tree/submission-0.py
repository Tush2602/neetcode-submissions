# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        if subRoot is None:
            return True
        def check(root, subroot):
            if root is None and subroot is None:
                return True
            if root is None or subroot is None:
                return False
            
            if root.val != subroot.val:
                return False 
            left = check(root.left, subroot.left)
            if not left:
                return False 

            right = check(root.right, subroot.right)
            if not right:
                return False 

            return True

        if root.val == subRoot.val:
            if check(root, subRoot):
                return True
        
        if self.isSubtree(root.right, subRoot):
            return True
        if self.isSubtree(root.left, subRoot):
            return True

        return False
