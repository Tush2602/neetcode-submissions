class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxm = [0] * n
        minm = [0] * n
        maxm[0] = nums[0]
        minm[0] = nums[0]
        ans = nums[0]

        for i in range(1, n):
            maxm[i] = max(nums[i], nums[i] * maxm[i-1], nums[i] * minm[i-1])
            minm[i] = min(nums[i], nums[i] * maxm[i-1], nums[i] * minm[i-1])

            ans = max(ans, maxm[i])
            
        return ans 