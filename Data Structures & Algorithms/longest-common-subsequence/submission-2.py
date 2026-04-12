class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1) + 1, len(text2) + 1
        LCS = [[0] * m for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                if text1[i - 1] == text2[j - 1]:
                    LCS[i][j] = LCS[i - 1][j - 1] + 1
                else:
                    LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

        return LCS[n - 1][m - 1]
                