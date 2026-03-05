class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        k = len(word)
        visited = [[False] * n for _ in range(m)]

        def backtrack(wordIdx, row, col) -> bool:
            if wordIdx == k:                         
                return True
            if row >= m or row < 0 or col >= n or col < 0:
                return False
            if visited[row][col]:
                return False
            if word[wordIdx] != board[row][col]:
                return False

            visited[row][col] = True                 

            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            solution = False
            for dr, dc in directions:
                solution = backtrack(wordIdx + 1, row + dr, col + dc)
                if solution:                          
                    break

            visited[row][col] = False                 
            return solution

        for i in range(m):
            for j in range(n):
                if backtrack(0, i, j):
                    return True
        return False