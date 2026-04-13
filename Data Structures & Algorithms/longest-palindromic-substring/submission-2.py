class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        maxLen = 1
        for j in range(n):
            # Diagonal
            dp[j][j] = True
            for i in range(0, j):
                # j = i + 1
                if j == i + 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        maxLen = max(maxLen, 2)
                # Else (j > i + 1)
                l = i + 1
                r = j - 1
                if l < n and r > 0 and l <= r:
                    if dp[l][r]:
                        if s[i] == s[j]:
                            dp[i][j] = True
                            maxLen = max(maxLen, j - i + 1)
                        else:
                            dp[i][j] = False
                    else:
                        dp[i][j] = False
        
        # Search maxLen palindrome
        for l in range(n):
            r = l + maxLen - 1
            if dp[l][r]:
                return s[l:r+1]