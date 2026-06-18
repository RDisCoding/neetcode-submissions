class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        negdiag = set()
        posdiag = set()

        res = []
        board = [["."]*n for i in range(n)]

        def bt(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for column in range(n):
                if column in cols or r+column in posdiag or r-column in negdiag:
                    continue
                cols.add(column)
                posdiag.add(r+column)
                negdiag.add(r-column)
                board[r][column] = "Q"

                bt(r+1)

                cols.remove(column)
                posdiag.remove(r+column)
                negdiag.remove(r-column)
                board[r][column] = "."

        bt(0)
        return res