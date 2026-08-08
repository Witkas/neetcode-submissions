class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [1e9] * (amount + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            for c in coins:
                remaining = i - c
                if remaining < 0:
                    continue
                else:
                    dp[i] = min(dp[i], 1 + dp[remaining])
        
        return dp[amount] if dp[amount] != 1e9 else -1