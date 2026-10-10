class Solution:
    def kthSmallest(self, root, k):
        count = 0
        answer = None

        def inorder(node):
            nonlocal count, answer

            if node is None:
                return

            inorder(node.left)

            count += 1
            if count == k:
                answer = node.val
                return

            inorder(node.right)

        inorder(root)
        return answer