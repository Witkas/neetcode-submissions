class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_nums = []
            col_nums = []
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row_nums:
                        return False
                    row_nums.append(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in col_nums:
                        return False
                    col_nums.append(board[j][i])
        
        bounds = [[0,1,2], [3,4,5], [6,7,8]]
        for b1 in bounds:
            for b2 in bounds:
                square_nums = []
                for i in b1:
                    for j in b2:
                        if board[i][j] != ".":
                            if board[i][j] in square_nums:
                                return False
                            square_nums.append(board[i][j])
        return True
