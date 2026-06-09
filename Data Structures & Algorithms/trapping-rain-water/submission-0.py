class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0
        
        for i in range(n):
            left_max = max(height[0:i+1])
            right_max = max(height[i:n])
            total += min(left_max, right_max) - height[i]
        
        return total