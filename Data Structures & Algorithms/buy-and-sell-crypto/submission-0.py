class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left, right =0 ,1
        profit =0
        while right < n:
            if prices[left] <=prices[right]:
                profit =max(profit, prices[right] - prices[left])
            right+=1

            if right == n:
                left = left + 1
                right = left + 1
            
        return profit