class Solution:
    # [5,1,5,6,7,1,10]
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 1

        while l < len(prices) and r < len(prices):
            profit = prices[r] - prices[l]
            if profit <= 0:
                l = r
            else:
                res = max(res, profit)
            r += 1
        return res