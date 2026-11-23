class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        current_row = defaultdict(set)
        current_col = defaultdict(set)
        all_sudoku = defaultdict(set)
        
        for r in range(0,9):
            for c in range(0,9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in current_row[r] or
                    board[r][c] in current_col[c] or
                    board[r][c] in all_sudoku[(r//3, c//3)]
                ):
                    return False
                current_row[r].add(board[r][c])
                current_col[c].add(board[r][c])
                all_sudoku[(r//3, c//3)].add(board[r][c])
        return True
        
            

                

