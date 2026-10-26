class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        def rec(n, dp):
            if n==1 or n ==0:
                return 1
            if dp[n] != -1:
                return dp[n] 
            dp[n] = rec(n-1, dp) + rec(n-2, dp)
            return dp[n]

        return rec(n, dp)