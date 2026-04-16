class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge Case
        if s[0] == "0":
            return 0
        
        # ASCII OFFSET
        OFFSET = 64
        n = len(s)
        dp = [0] * n
        dp[0] = 1

        # Update DP Table
        for i in range(1, n):
            # Number of decodes with last digit decoded as one letter
            if s[i] != "0":
                dp[i] += dp[i - 1]
            # Number of decodes with last two digits together decoded as one letter
            if 10 <= int(s[i-1:i+1]) <= 26:
                # second index not defined yet
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]

        return dp[n - 1]