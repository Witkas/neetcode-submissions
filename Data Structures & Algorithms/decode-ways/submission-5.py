class Solution:
    # "10123"
    # /    \
    # "1"   "10"
    # / \   /     \
    # X X   "10+1" "10+12"
    #        /    \
    #      "10+1+2" X    

    # dp = {0: 0, ... , 5: 1}

    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            if i not in dp:
                dp[i] = 0
            else:
                return dp[i]
            if s[i] != "0":
                dp[i] += dfs(i+1)
            if i < len(s) - 1 and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dfs(i+2)
            return dp[i]
        
        return dfs(0)
