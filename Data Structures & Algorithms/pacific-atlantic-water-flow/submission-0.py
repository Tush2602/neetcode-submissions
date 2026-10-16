class Solution:
    def dfs(self, grid, r, c, is_visited):
        is_visited[r][c] = True
        for x_, y_ in [(-1,0), (0,-1), (0,1), (1,0)]:
            xx, yy = r + x_, c + y_
            if xx < 0 or yy < 0 or xx > len(grid)-1 or yy> len(grid[0])-1:
                continue 
            if is_visited[xx][yy] == True:
                continue
            if grid[xx][yy] >= grid[r][c]:
                self.dfs(grid, xx, yy, is_visited)


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        row_len, col_len = len(heights), len(heights[0])
        pacific_mat = [[False for _ in range(col_len)] for _ in range(row_len)]
        atlantic_mat = [[False for _ in range(col_len)] for _ in range(row_len)]

        for row in range(row_len):
            for col in range(col_len):
                self.dfs(heights, 0, col, pacific_mat)
                self.dfs(heights, row, 0, pacific_mat)
                self.dfs(heights, row_len-1, col, atlantic_mat)
                self.dfs(heights, row, col_len -1, atlantic_mat)

        result = []
        for row in range(row_len):
            for col in range(col_len):
                if pacific_mat[row][col] == True and atlantic_mat[row][col]==True:
                    result.append([row, col])

        return result 

                
                

                
        

