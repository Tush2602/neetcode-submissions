class Solution:
    def climbStairs(self, n: int) -> int:
        temp1 = 0
        temp2 = 1

        for i in range(1, n+1):
            dp = temp1 + temp2
            temp1 = temp2
            temp2 = dp

        return temp2 