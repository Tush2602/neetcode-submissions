from collections import deque
class Solution:
    def bfs(self, grid, visited, r, c):
        queue = deque()
        visited[r][c] = True
        queue.append((r, c))
        count = 1

        while queue:
            x, y = queue.popleft()
            for x_ , y_ in [(0,-1), (-1, 0), (1, 0), (0,1)]:
                xx, yy = x+ x_ , y+y_
                if xx < 0 or yy < 0 or xx > len(grid)-1 or yy > len(grid[0])-1:
                    continue
                if visited[xx][yy] == True:
                    continue
                if grid[xx][yy] == 0:
                    continue    
                queue.append((xx, yy))
                visited[xx][yy] = True
                count+=1

        return count

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
                    max_land = max(max_land, self.bfs(grid, visited, row, col))

        return max_land      