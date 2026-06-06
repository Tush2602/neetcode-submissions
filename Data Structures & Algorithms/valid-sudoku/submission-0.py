class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rem_dots = [x for x in row if x!="."]
            if len(rem_dots) != len(set(rem_dots)):
                return False

        for column in zip(*board):
            rem_dots = [x for x in column if x!="."]
            if len(rem_dots) != len(set(rem_dots)):
                return False

        for rows in range(0, 9, 3):
            for col in range(0, 9, 3):
                box= [x for row in board[rows:rows+3] for x in row[col:col+3]]
                rem_dots = [x for x in box if x!= "."]
                if len(rem_dots) != len(set(rem_dots)):
                    return False

        return True
        
        
        