from collections import deque

class Solution:
    def bfs(self, grid, visited, r, c):
        queue = deque()
        visited[r][c] = True
        queue.append((r, c))

        while queue:
            x, y = queue.popleft()
            for x_,y_ in [(-1,0), (0, -1), (1, 0), (0,1)]:
                xx, yy = x_ + x, y_ +y
                if xx < 0 or yy < 0 or xx> len(grid) -1 or yy > len(grid[0])-1:
                    continue
                if visited[xx][yy] ==True:
                    continue
                if grid[xx][yy] == '0':
                    continue
                visited[xx][yy] = True
                queue.append((xx, yy))
                

    def numIslands(self, grid: List[List[str]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        count = 0

        visited = [[False for _ in range(col_len)] for _ in range(row_len)]

        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] =='1' and visited[row][col] == False:
                    count+=1
                    self.bfs(grid, visited, row, col)
        return count



        

        