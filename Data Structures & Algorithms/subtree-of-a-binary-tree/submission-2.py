# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 

    def preorder(self, root, result: List):
        if root is None:
            result.append("#")
            return 
        result.append(str(root.val))
        self.preorder(root.left, result)
        self.preorder(root.right, result)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        tree = []
        self.preorder(root, tree)
        subtree = []
        self.preorder(subRoot, subtree)

        for i in range(len(tree) - len(subtree) + 1):
            if tree[i:i + len(subtree)] == subtree:
                return True

        return False

        
