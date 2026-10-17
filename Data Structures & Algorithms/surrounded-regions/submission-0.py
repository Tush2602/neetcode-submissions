from collections import deque

class Solution:
    def bfs(self, grid, row, col, is_visited):
        if is_visited[row][col]==True or grid[row][col]=="X":
            return 
        queue = deque()
        queue.append((row, col))

        is_visited[row][col] = True

        while queue:
            x, y= queue.popleft()
            for x_, y_ in [(-1,0), (0, -1), (0,1), (1,0)]:
                xx, yy = x + x_, y+ y_
                if xx < 0 or yy < 0 or xx > len(grid) -1 or yy> len(grid[0]) - 1:
                    continue
                if is_visited[xx][yy] ==True:
                    continue
                if grid[xx][yy] == "O":
                    is_visited[xx][yy]= True
                    queue.append((xx,yy))

        
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return []

        row_len, col_len = len(board), len(board[0])
        is_visited = [[False for _ in range(col_len)] for _ in range(row_len)]

        for row in range(row_len):
            for col in range(col_len):
                self.bfs(board, 0, col, is_visited)
                self.bfs(board, row_len-1, col, is_visited)
                self.bfs(board, row, 0, is_visited)
                self.bfs(board, row, col_len-1, is_visited)

        for row in range(row_len):
            for col in range(col_len):
                if board[row][col] == "O" and is_visited[row][col] == False:
                    board[row][col] ="X"

