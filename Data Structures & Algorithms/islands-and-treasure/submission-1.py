from collections import deque

class Node:
    def __init__(self, row : int, col: int, distance :int = 0):
        self.row = row
        self.col = col
        self.distance = distance


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if grid is None:
            return None
        
        queue = deque()
        row_len, col_len = len(grid), len(grid[0])

        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 0:
                    queue.append(Node(row, col, 0))

        while queue:
            root = queue.popleft()
            for x_, y_ in [(-1,0), (0, -1), (0,1), (1,0)]:
                xx, yy = root.row+x_, root.col+y_
                if xx < 0 or yy < 0 or xx > row_len -1 or yy> col_len -1:
                    continue 
                if grid[xx][yy] == -1:
                    continue
                if grid[xx][yy] == 2147483647:
                    grid[xx][yy] = root.distance + 1
                    queue.append(Node(xx, yy, root.distance +1))


                