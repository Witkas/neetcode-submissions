# [30,38,30,36,35,40,28]
# [1,4,1,2,1,0,0]


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dp = [0] * len(temperatures)

        for i in range(len(temperatures) - 2, -1, -1):
            j = i + 1
            while temperatures[i] >= temperatures[j] and j < len(temperatures):
                if dp[j] == 0:
                    j = i
                    break
                j += dp[j]
            dp[i] = j - i

        return dp