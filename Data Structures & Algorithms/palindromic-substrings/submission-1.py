class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # i = row index
        # j = col index
        count = 0
        for j in range(n):
            # Diagonals always true and increment
            dp[j][j] = True
            count += 1
            # Fill the table column by column
            for i in range(j):
                if s[i] == s[j]:
                    # length two substring
                    if j == i + 1:
                        dp[i][j] = True
                        count += 1
                        continue
                    # length > 2 substring
                    l = i + 1
                    r = j - 1
                    if dp[l][r]:
                        dp[i][j] = True
                        count += 1
                else:
                    continue
        return count