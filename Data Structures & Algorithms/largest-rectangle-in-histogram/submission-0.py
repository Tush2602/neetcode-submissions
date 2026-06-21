class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        A = 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, ht = stack.pop()
                A = max(A, ht * (i - idx))
                start = idx

            stack.append((start, h))

        for i, h in stack:
            A = max(A, h * (len(heights) - i))
        return A
        