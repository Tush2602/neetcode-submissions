# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        def kth(root, result):
            if root is None:
                return 
            kth(root.left, result)
            result.append(root.val)
            kth(root.right, result)
        
        kth(root, result)
        return result[k-1]