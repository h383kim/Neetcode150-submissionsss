class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge Case
        if s[0] == "0":
            return 0
        
        # ASCII OFFSET
        OFFSET = 64
        n = len(s)
        dp1 = 0
        dp2 = 1
        
        cur_dp = 0
        # Update DP Table
        for i in range(1, n):
            # Number of decodes with last digit decoded as one letter
            if s[i] != "0":
                cur_dp += dp2
            # Number of decodes with last two digits together decoded as one letter
            if 10 <= int(s[i-1:i+1]) <= 26:
                # second index not defined yet
                if i == 1:
                    cur_dp += 1
                else:
                    cur_dp += dp1
            cur_dp, dp1, dp2 = 0, dp2, cur_dp

        return dp2