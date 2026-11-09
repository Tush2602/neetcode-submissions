class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def cnt(amt, coins):
            if amt == 0 :
                return 0
            if amt < 0:
                return float("inf")
            if amt in memo:
                return memo[amt]
            val= []
            for coin in coins:
                ways = cnt(amt-coin, coins)
                val.append(ways)
            memo[amt] =  1 + min(val)
            return memo[amt]
        ans = cnt(amount, coins)
        return -1 if ans== float('inf') else ans
            