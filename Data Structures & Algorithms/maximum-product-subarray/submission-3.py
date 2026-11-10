class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prev_maxm = nums[0]
        prev_minm = nums[0]
        ans = nums[0]
        maxm,minm = 0,0
        for i in range(1, n):
            maxm = max(nums[i], nums[i] * prev_maxm, nums[i] * prev_minm)
            minm= min(nums[i], nums[i] * prev_maxm, nums[i] * prev_minm)
            prev_maxm, prev_minm= maxm, minm
            ans = max(ans, maxm)
            
        return ans 