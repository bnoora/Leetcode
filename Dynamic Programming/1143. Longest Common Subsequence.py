class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS = len(text1)
        COLS = len(text2)
        memo = [[0]*(COLS+1) for _ in range(ROWS+1)]
        for i in reversed(range(ROWS)):
            for j in reversed(range(COLS)):
                if text1[i] == text2[j]:
                    memo[i][j] = 1 + memo[i+1][j+1]
                else:
                    memo[i][j] = max(memo[i+1][j], memo[i][j+1])

        return memo[0][0]
