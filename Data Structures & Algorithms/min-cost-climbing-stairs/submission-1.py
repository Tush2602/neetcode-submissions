class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        temp = [-1] * (n+1)
        def dp(i):
            if i >= n:
                return 0
            if temp[i] != -1:
                return temp[i]
            temp[i] = cost[i] + min(dp(i+1), dp(i+2))
            return temp[i]
        return min(dp(0), dp(1))
            