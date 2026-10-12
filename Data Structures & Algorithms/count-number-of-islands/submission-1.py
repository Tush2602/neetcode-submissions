from collections import deque

class Solution:
    def dfs(self, grid, visited, r, c):
        if r < 0 or c <0 or r > len(grid)-1 or c > len(grid[0]) - 1:
            return 
        if visited[r][c] == True:
            return 
        if grid[r][c] == '0':
            return 
        visited[r][c] = True
        self.dfs(grid, visited, r, c-1) 
        self.dfs(grid, visited, r-1, c) 
        self.dfs(grid, visited, r+1, c) 
        self.dfs(grid, visited, r, c+1) 
                

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row_len = len(grid)
        col_len = len(grid[0])
        count = 0

        visited = [[False for _ in range(col_len)] for _ in range(row_len)]

        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] =='1' and visited[row][col] == False:
                    count+=1
                    self.dfs(grid, visited, row, col)
        return count



        

        