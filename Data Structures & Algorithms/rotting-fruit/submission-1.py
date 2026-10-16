from collections import deque
class Node:
    def __init__(self, row : int, col : int, time: int = 0):
        self.row = row
        self.col = col
        self.time = time
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid is []:
            return 0
        queue = deque()
        row_len, col_len = len(grid), len(grid[0])
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 2:
                    queue.append(Node(row, col, 0))
        min_time = 0        
        while queue:
            root = queue.popleft()

            x, y = root.row, root.col
            for x_, y_ in [(-1,0), (0, -1), (0, 1), (1,0)]:
                xx, yy = x + x_, y+y_
                if xx < 0 or yy < 0 or xx > row_len - 1 or yy > col_len-1:
                    continue
                if grid[xx][yy] == 0:
                    continue
                if grid[xx][yy] ==1:
                    min_time = max(min_time, root.time+1)
                    grid[xx][yy] = 2
                    queue.append(Node(xx, yy, root.time+ 1))
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col]==1:
                    return -1
        return min_time
                
                    
