class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posdiag = set() # r+c same
        negdiag = set() # r-c same

        board = [["."]*n for i in range(n)]
        res = []

        def bt(i):
            if i == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (i+c) in posdiag or (i-c) in negdiag:
                    continue
                
                col.add(c)
                posdiag.add(i+c)
                negdiag.add(i-c)
                board[i][c] = "Q"

                bt(i+1)

                col.remove(c)
                posdiag.remove(i+c)
                negdiag.remove(i-c)
                board[i][c] = "."
                
        bt(0)
        return res