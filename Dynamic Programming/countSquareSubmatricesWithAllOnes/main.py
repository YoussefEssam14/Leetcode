
class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        """
        dp[i][j] -> number of square submatrices with all ones ending at i , j
        i.e have matrix[i][j] as bottom-right corner
        if matrix[i][j] == 1
            then dp[i][j] = 1 (intutively this square contribute ) + min(top,left,top-left)
        """
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        return sum(sum(row) for row in dp)