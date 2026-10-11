# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hash_map = {val : i for i, val in enumerate(inorder)}
        pre_idx = 0
        
        def BTree(l, r):
            nonlocal pre_idx
            if l > r:
                return None

            val = preorder[pre_idx]
            pre_idx+=1

            node = TreeNode(val)
            in_idx = hash_map[val]
            node.left = BTree(l, in_idx-1)
            node.right = BTree(in_idx+1, r)

            return node
        
        return BTree(0, len(inorder)-1)
