class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(i,j):
            if i<0 or j<0 or i==rows or j==cols or board[i][j] == 'X' or board[i][j] == '#' :
                return
            
            if board[i][j] == "O":
                board[i][j] = "#"
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)

        for i in [0, rows-1]:
            for j in range(cols):
                if board[i][j] == "O":
                    dfs(i,j)
                
        for i in range(rows):
            for j in [0, cols-1]:
                if board[i][j] == "O":
                    dfs(i,j)
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] != "#":
                    board[i][j] = "X"
                else:
                    board[i][j] = "O"