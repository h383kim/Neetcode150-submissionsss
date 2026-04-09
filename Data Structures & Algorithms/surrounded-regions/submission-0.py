class Solution:
    def solve(self, board: List[List[str]]) -> None:
        nrow, ncol = len(board), len(board[0])

        def find(i, j):
            if i < 0 or i == nrow:
                return
            if j < 0 or j == ncol:
                return
            if board[i][j] != 'O':
                return

            board[i][j] = '#'
            
            find(i - 1, j)
            find(i + 1, j)
            find(i, j - 1)
            find(i, j + 1)


        
        # Top
        for c in range(ncol):
            if board[0][c] == "O":
                find(0, c)
            
        # Bottom
        for c in range(ncol):
            if board[nrow - 1][c] == "O":
                find(nrow - 1, c)

        # Left
        for r in range(nrow):
            if board[r][0] == "O":
                find(r, 0)

        # Right
        for r in range(nrow):
            if board[r][ncol - 1] == "O":
                find(r, ncol - 1)

        for r in range(nrow):
            for c in range(ncol):
                if board[r][c] == '#':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'
        
