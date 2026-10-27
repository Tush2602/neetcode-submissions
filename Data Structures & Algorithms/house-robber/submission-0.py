class Solution:
    def rob(self, nums: List[int]) -> int:
        n =len(nums)
        dp = [-1] * (n+1)
        def amt(n):
            if n <= 0:
                return 0
            if dp[n] != -1:
                return dp[n]
            take = nums[n-1] + amt(n-2)
            skip = amt(n-1) 
            dp[n] = max(take, skip)
            return dp[n]
        
        return amt(n)