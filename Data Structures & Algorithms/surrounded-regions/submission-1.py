from collections import deque

class Solution:
    def bfs(self, grid, row, col):
        if grid[row][col]=='S' or grid[row][col]=="X":
            return 
        queue = deque()
        queue.append((row, col))

        grid[row][col] = 'S'

        while queue:
            x, y= queue.popleft()
            for x_, y_ in [(-1,0), (0, -1), (0,1), (1,0)]:
                xx, yy = x + x_, y+ y_
                if xx < 0 or yy < 0 or xx > len(grid) -1 or yy> len(grid[0]) - 1:
                    continue
                if grid[xx][yy] =='S':
                    continue
                if grid[xx][yy] == "O":
                    grid[xx][yy]= 'S'
                    queue.append((xx,yy))

        
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return []

        row_len, col_len = len(board), len(board[0])

        for col in range(col_len):
            self.bfs(board, 0, col)
            self.bfs(board, row_len - 1, col)

        for row in range(row_len):
            self.bfs(board, row, 0)
            self.bfs(board, row, col_len - 1)

        for row in range(row_len):
            for col in range(col_len):
                if board[row][col] == "O":
                    board[row][col] ="X"

        for row in range(row_len):
            for col in range(col_len):
                if board[row][col] == "S":
                    board[row][col] ="O"

        

