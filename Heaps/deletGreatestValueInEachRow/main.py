class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        for i in range(len(grid)):
            grid[i].sort()
        grid = list(zip(*grid))
        return sum(max(row) for row in grid)