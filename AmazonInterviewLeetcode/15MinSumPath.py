#https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid):
        row = len(grid)
        column = len(grid[0])

        for i in range(1, column):
            grid[0][i] += grid[0][i - 1]

        for i in range(1, row):
            grid[i][0] += grid[i - 1][0]
            for j in range(1, column):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[row - 1][column - 1]