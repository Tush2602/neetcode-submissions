
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        case1 = self.rob_linear(nums[:-1])
        case2 = self.rob_linear(nums[1:])

        return max(case1, case2)

    def rob_linear(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n + 1)

        def solve(i):
            if i <= 0:
                return 0

            if dp[i] != -1:
                return dp[i]

            take = nums[i - 1] + solve(i - 2)
            skip = solve(i - 1)

            dp[i] = max(take, skip)
            return dp[i]

        return solve(n)
