from collections import deque
class Solution:
    def dfs(self, grid, visited, r, c):
        if r < 0 or c <0 or r > len(grid)-1 or c > len(grid[0])-1:
            return 0
        if visited[r][c] == True:
            return 0
        if grid[r][c] == 0:
            return 0
        visited[r][c] = True
        area = 1
        area+=self.dfs(grid, visited, r, c-1)
        area+=self.dfs(grid, visited, r-1, c)
        area+=self.dfs(grid, visited, r+1, c)
        area+=self.dfs(grid, visited, r, c+1)

        return area 
        

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        row_len = len(grid)
        col_len = len(grid[0])
        max_land = 0

        visited = [[False for _ in range(col_len)] for _ in range(row_len)]

        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 1 and visited[row][col] == False:
                    max_land = max(max_land, self.dfs(grid, visited, row, col))

        return max_land      